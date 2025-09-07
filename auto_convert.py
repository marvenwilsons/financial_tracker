#!/usr/bin/env python3
"""
Credit Card Data Converter - Auto Mode
Automatically converts all credit card data files
"""

import csv
import os
from datetime import datetime

def convert_date_format(date_str):
    """Convert YYYY-MM-DD to MM/DD/YYYY format"""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%m/%d/%Y')
    except ValueError:
        return date_str

def convert_single_file(input_file, output_file, starting_balance=0.0):
    """Convert a single credit card CSV file"""

    converted_transactions = []
    current_balance = starting_balance

    print(f"Converting {os.path.basename(input_file)}...")

    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                date = row['Date']
                description = row['Description']
                amount = float(row['Amount'])

                # Convert date format
                app_date = convert_date_format(date)

                # Clean description
                clean_description = description.replace("'", "").replace('"', '')

                # Determine withdrawn vs deposited amounts
                if amount < 0:
                    # Payment (reduces balance)
                    withdrawn_amount = 0
                    deposited_amount = abs(amount)
                    current_balance -= abs(amount)
                else:
                    # Charge (increases balance)
                    withdrawn_amount = amount
                    deposited_amount = 0
                    current_balance += amount

                # Create transaction in app format
                converted_transaction = {
                    'date': app_date,
                    'description': clean_description,
                    'withdrawn_amount': withdrawn_amount,
                    'deposited_amount': deposited_amount,
                    'balance_amount': round(current_balance, 2)
                }

                converted_transactions.append(converted_transaction)

        # Write converted data
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['date', 'description', 'withdrawn_amount', 'deposited_amount', 'balance_amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for transaction in converted_transactions:
                writer.writerow(transaction)

        print(f"   ✅ {len(converted_transactions)} transactions converted")
        print(f"   💰 Final balance: ${current_balance:.2f}")

        return current_balance

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return starting_balance

def main():
    """Convert all files automatically"""

    # Input files
    input_files = [
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/credit_card_transactions_2019_full.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2020.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2021.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2022.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2023.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2024.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2025.csv'
    ]

    # Create output directory
    output_dir = '/Users/marvenwilsondonque/code/financial_tracker/converted_data'
    os.makedirs(output_dir, exist_ok=True)

    print("🔄 CONVERTING CREDIT CARD DATA TO APP FORMAT")
    print("=" * 50)

    running_balance = 0.0

    for input_file in input_files:
        if not os.path.exists(input_file):
            print(f"⚠️  Skipping {os.path.basename(input_file)} - file not found")
            continue

        # Extract year from filename
        if '2019_full' in input_file:
            year = '2019'
        else:
            year = input_file.split('_')[-1].split('.')[0]

        output_file = os.path.join(output_dir, f'app_ready_{year}.csv')

        running_balance = convert_single_file(input_file, output_file, running_balance)
        print()

    # Create a sample test file
    sample_file = os.path.join(output_dir, 'sample_test.csv')
    sample_data = """01/15/2025,'Test Transaction 1',25.99,0,25.99
01/16/2025,'Test Payment',0,50.00,-24.01
01/17/2025,'Test Purchase',15.50,0,-8.51"""

    with open(sample_file, 'w') as f:
        f.write(sample_data)

    print("🎉 CONVERSION COMPLETE!")
    print(f"📁 Files saved to: {output_dir}")
    print()
    print("📋 NEXT STEPS:")
    print("1. Open your financial tracker app at http://localhost:3000")
    print("2. Go to the 'Add Statement' page")
    print("3. Select 'Credit Statement' as the statement type")
    print("4. Copy and paste the content from any converted file")
    print("5. The app will parse and validate the data")
    print()
    print("💡 TIP: Start with sample_test.csv to test the functionality first")

if __name__ == "__main__":
    main()
