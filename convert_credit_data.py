#!/usr/bin/env python3
"""
Credit Card Data Converter for Financial Tracker App
Converts credit card CSV data to the format expected by the financial tracker application
"""

import csv
import sys
from datetime import datetime
import os

def convert_date_format(date_str):
    """Convert YYYY-MM-DD to MM/DD/YYYY format"""
    try:
        # Parse the date
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        # Return in MM/DD/YYYY format
        return date_obj.strftime('%m/%d/%Y')
    except ValueError:
        # If parsing fails, return original
        return date_str

def convert_credit_card_to_app_format(input_file, output_file, running_balance=0.0):
    """
    Convert credit card CSV to financial tracker app format

    Args:
        input_file: Path to credit card CSV file
        output_file: Path to output CSV file
        running_balance: Starting balance for calculations
    """

    converted_transactions = []
    current_balance = running_balance

    print(f"Converting {input_file}...")

    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            date = row['Date']
            description = row['Description']
            amount = float(row['Amount'])

            # Convert date format
            app_date = convert_date_format(date)

            # Clean description (remove special characters that might cause issues)
            clean_description = description.replace("'", "").replace('"', '')

            # Determine if it's a payment (negative) or charge (positive)
            if amount < 0:
                # Payment - this goes to deposited_amount
                withdrawn_amount = 0
                deposited_amount = abs(amount)
                current_balance -= abs(amount)  # Payments reduce credit card balance
            else:
                # Charge - this goes to withdrawn_amount
                withdrawn_amount = amount
                deposited_amount = 0
                current_balance += amount  # Charges increase credit card balance

            # Create the app-format transaction
            converted_transaction = {
                'date': app_date,
                'description': clean_description,
                'withdrawn_amount': withdrawn_amount,
                'deposited_amount': deposited_amount,
                'balance_amount': round(current_balance, 2)
            }

            converted_transactions.append(converted_transaction)

    # Write to output file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'description', 'withdrawn_amount', 'deposited_amount', 'balance_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Don't write header - the app expects raw CSV data
        for transaction in converted_transactions:
            writer.writerow(transaction)

    print(f"✅ Converted {len(converted_transactions)} transactions")
    print(f"📁 Output saved to: {output_file}")
    print(f"💰 Final balance: ${current_balance:.2f}")

    return converted_transactions, current_balance

def batch_convert_all_files():
    """Convert all credit card files in batch"""

    # Define input files
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

    running_balance = 0.0  # Start with 0 balance

    print("🔄 BATCH CONVERTING CREDIT CARD DATA")
    print("=" * 50)

    for input_file in input_files:
        if not os.path.exists(input_file):
            print(f"⚠️  File not found: {input_file}")
            continue

        # Extract year from filename
        if '2019_full' in input_file:
            year = '2019'
        else:
            year = input_file.split('_')[-1].split('.')[0]

        output_file = os.path.join(output_dir, f'converted_credit_statements_{year}.csv')

        try:
            transactions, running_balance = convert_credit_card_to_app_format(
                input_file, output_file, running_balance
            )
            print(f"   Running balance after {year}: ${running_balance:.2f}")
            print()
        except Exception as e:
            print(f"❌ Error converting {input_file}: {e}")
            print()

    print("🎉 CONVERSION COMPLETE!")
    print(f"📁 All converted files saved to: {output_dir}")
    print(f"💡 You can now upload these files to your financial tracker app")

def create_sample_for_testing():
    """Create a small sample file for testing the app"""

    sample_data = [
        "01/15/2025,'Netflix Subscription',18.99,0,18.99",
        "01/16/2025,'Grocery Store',75.50,0,94.49",
        "01/17/2025,'Payment Thank You',0,100.00,-5.51",
        "01/18/2025,'Gas Station',45.00,0,39.49",
        "01/19/2025,'Coffee Shop',5.75,0,45.24"
    ]

    output_file = '/Users/marvenwilsondonque/code/financial_tracker/sample_test_data.csv'

    with open(output_file, 'w') as f:
        for line in sample_data:
            f.write(line + '\n')

    print(f"📝 Sample test file created: {output_file}")
    print("🧪 Use this file to test the app upload functionality first")

def main():
    """Main function"""
    print("💳 CREDIT CARD DATA CONVERTER")
    print("=" * 40)
    print()
    print("This script converts your credit card CSV data to the format")
    print("expected by your financial tracker application.")
    print()

    choice = input("Choose an option:\n1. Convert all files\n2. Create test sample\n3. Convert single file\nEnter choice (1-3): ")

    if choice == '1':
        batch_convert_all_files()
    elif choice == '2':
        create_sample_for_testing()
    elif choice == '3':
        input_file = input("Enter path to input CSV file: ")
        output_file = input("Enter path to output CSV file: ")
        if os.path.exists(input_file):
            convert_credit_card_to_app_format(input_file, output_file)
        else:
            print(f"❌ File not found: {input_file}")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
