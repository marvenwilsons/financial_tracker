#!/bin/bash

# Import all converted CSV files into the database

DB_NAME="money"
DB_USER="postgres"
CONTAINER_NAME="financial_tracker_db"

echo "Starting data import..."

# Get the default user ID first
USER_ID=$(docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -t -c "SELECT user_id FROM users LIMIT 1;" | tr -d ' ')

if [ -z "$USER_ID" ]; then
    echo "No user found in database. Creating default user..."
    docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "INSERT INTO users (user_id, name, email) VALUES (uuid_generate_v4(), 'Default User', 'user@example.com');"
    USER_ID=$(docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -t -c "SELECT user_id FROM users LIMIT 1;" | tr -d ' ')
fi

echo "Using user ID: $USER_ID"

for file in converted_data/app_ready_*.csv; do
    if [ -f "$file" ]; then
        echo "Importing $file..."
        # CSV format: date,description,withdrawn_amount,deposited_amount,balance_amount
        # Map to: date,description,statement_type,withdrawn_amount,deposited_amount,balance_amount,statement_owner
        awk -F',' -v user_id="$USER_ID" 'BEGIN{OFS=","} {
            # Determine transaction type based on amounts
            if ($3 > 0) type="withdrawal"
            else if ($4 > 0) type="deposit"
            else type="other"

            print $1, $2, type, $3, $4, $5, user_id
        }' "$file" > /tmp/temp_import.csv

        docker exec -i $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "\COPY statement(date, description, statement_type, withdrawn_amount, deposited_amount, balance_amount, statement_owner) FROM STDIN WITH CSV;" < /tmp/temp_import.csv

        if [ $? -eq 0 ]; then
            echo "✓ Successfully imported $file"
        else
            echo "✗ Failed to import $file"
        fi
    fi
done

echo "Data import completed!"

# Check total records
echo "Total records in database:"
docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "SELECT COUNT(*) FROM statement;"
