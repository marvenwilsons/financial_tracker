#!/bin/bash

# Import all converted CSV files into the database

DB_NAME="money"
DB_USER="postgres"
CONTAINER_NAME="financial_tracker_db"

echo "Starting data import..."

# Get the default user ID first
USER_ID=$(docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -t -c "SELECT user_id FROM users LIMIT 1;" | tr -d ' \r\n')

if [ -z "$USER_ID" ]; then
    echo "No user found in database. Creating default user..."
    docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "INSERT INTO users (user_id, name, email) VALUES (uuid_generate_v4(), 'Default User', 'user@example.com');"
    USER_ID=$(docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -t -c "SELECT user_id FROM users LIMIT 1;" | tr -d ' \r\n')
fi

echo "Using user ID: $USER_ID"

for file in converted_data/app_ready_*.csv; do
    if [ -f "$file" ]; then
        echo "Importing $file..."

        # Create temporary file with proper format
        temp_file="/tmp/temp_import_$(basename $file).csv"

        while IFS=',' read -r date description withdrawn deposited balance; do
            # Remove any carriage returns
            date=$(echo "$date" | tr -d '\r')
            description=$(echo "$description" | tr -d '\r')
            withdrawn=$(echo "$withdrawn" | tr -d '\r')
            deposited=$(echo "$deposited" | tr -d '\r')
            balance=$(echo "$balance" | tr -d '\r')

            # Determine transaction type based on amounts
            if [[ $(echo "$withdrawn > 0" | bc -l) -eq 1 ]]; then
                type="withdrawal"
            elif [[ $(echo "$deposited > 0" | bc -l) -eq 1 ]]; then
                type="deposit"
            else
                type="other"
            fi

            echo "$date,$description,$type,$withdrawn,$deposited,$balance,$USER_ID" >> "$temp_file"
        done < "$file"

        # Import the temporary file
        docker cp "$temp_file" $CONTAINER_NAME:/tmp/import.csv
        docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "\COPY statement(date, description, statement_type, withdrawn_amount, deposited_amount, balance_amount, statement_owner) FROM '/tmp/import.csv' WITH CSV;"

        if [ $? -eq 0 ]; then
            echo "✓ Successfully imported $file"
        else
            echo "✗ Failed to import $file"
        fi

        # Clean up
        rm -f "$temp_file"
        docker exec $CONTAINER_NAME rm -f /tmp/import.csv
    fi
done

echo "Data import completed!"

# Check total records
echo "Total records in database:"
docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "SELECT COUNT(*) FROM statement;"
