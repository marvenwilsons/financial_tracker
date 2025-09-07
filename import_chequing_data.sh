#!/bin/bash

# Create chequing_statements table
docker exec financial_tracker_db psql -U postgres -d money -c "
CREATE TABLE IF NOT EXISTS chequing_statements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    date DATE NOT NULL,
    description TEXT,
    withdrawn_amount MONEY DEFAULT 0,
    deposited_amount MONEY DEFAULT 0,
    balance_amount MONEY DEFAULT 0,
    account_type VARCHAR(20) DEFAULT 'Chequing',
    statement_owner UUID,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"

echo "Created chequing_statements table"

# Function to import CSV file
import_chequing_csv() {
    local csv_file=$1
    local year=$2

    echo "Importing $csv_file for year $year..."

    # Copy file to container and import
    docker cp "$csv_file" financial_tracker_db:/tmp/chequing_$year.csv

    docker exec financial_tracker_db psql -U postgres -d money -c "
    COPY chequing_statements (date, description, withdrawn_amount, deposited_amount, balance_amount, account_type)
    FROM '/tmp/chequing_$year.csv'
    WITH CSV HEADER;
    "

    echo "Imported $csv_file successfully"
}

# Import all chequing CSV files
import_chequing_csv "/Users/marvenwilsondonque/code/financial_tracker/chequing_data/Chequing_Transactions_2019.csv" "2019"
import_chequing_csv "/Users/marvenwilsondonque/code/financial_tracker/chequing_data/Chequing_Transactions_2020.csv" "2020"
import_chequing_csv "/Users/marvenwilsondonque/code/financial_tracker/chequing_data/Chequing_Transactions_2021.csv" "2021"
import_chequing_csv "/Users/marvenwilsondonque/code/financial_tracker/chequing_data/chequing_transactions_2022.csv" "2022"
import_chequing_csv "/Users/marvenwilsondonque/code/financial_tracker/chequing_data/Chequing_Transactions_2023.csv" "2023"
import_chequing_csv "/Users/marvenwilsondonque/code/financial_tracker/chequing_data/Chequing_Transactions_2025.csv" "2025"

echo "All chequing data imported successfully!"

# Show summary
docker exec financial_tracker_db psql -U postgres -d money -c "
SELECT
    EXTRACT(YEAR FROM date) as year,
    COUNT(*) as transaction_count,
    SUM(deposited_amount::numeric) as total_deposits,
    MIN(date) as earliest_date,
    MAX(date) as latest_date
FROM chequing_statements
GROUP BY EXTRACT(YEAR FROM date)
ORDER BY year;
"
