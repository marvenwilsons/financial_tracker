#!/usr/bin/env python3
"""
Credit Card Transaction Analysis Script
Analyzes spending patterns across multiple years of credit card data
"""

import pandas as pd
import numpy as np
from datetime import datetime
import re
from collections import defaultdict, Counter

def load_and_analyze_transactions():
    """Load all transaction files and perform comprehensive analysis"""
    
    # File paths
    files = [
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/credit_card_transactions_2019_full.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2020.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2021.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2022.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2023.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2024.csv',
        '/Users/marvenwilsondonque/Desktop/pivot/marven/Finanance/Extracted_Credit_Card_Transactions_2025.csv'
    ]
    
    all_data = []
    yearly_stats = {}
    
    print("=== LOADING TRANSACTION DATA ===")
    for file in files:
        try:
            df = pd.read_csv(file)
            year = file.split('_')[-1].split('.')[0]
            if 'full' in year:
                year = '2019'
            
            df['Year'] = year
            df['Date'] = pd.to_datetime(df['Date'])
            df['Month'] = df['Date'].dt.month
            df['MonthName'] = df['Date'].dt.month_name()
            
            all_data.append(df)
            yearly_stats[year] = {
                'transactions': len(df),
                'spending': df[df['Amount'] > 0]['Amount'].sum(),
                'payments': abs(df[df['Amount'] < 0]['Amount'].sum()),
                'net': df['Amount'].sum()
            }
            
            print(f"{year}: {len(df)} transactions")
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    # Combine all data
    df_all = pd.concat(all_data, ignore_index=True)
    
    print(f"\n=== OVERALL STATISTICS ===")
    print(f"Total transactions: {len(df_all)}")
    print(f"Date range: {df_all['Date'].min().strftime('%Y-%m-%d')} to {df_all['Date'].max().strftime('%Y-%m-%d')}")
    print(f"Total spending: ${df_all[df_all['Amount'] > 0]['Amount'].sum():,.2f}")
    print(f"Total payments: ${abs(df_all[df_all['Amount'] < 0]['Amount'].sum()):,.2f}")
    print(f"Net amount: ${df_all['Amount'].sum():,.2f}")
    
    return df_all, yearly_stats

def categorize_transactions(df):
    """Categorize transactions based on description patterns"""
    
    categories = {
        'Food & Dining': [
            'MCDONALD', 'TIM HORTONS', 'SUBWAY', 'THAI EXPRESS', 'STARBUCKS',
            'JOLLIBEE', 'KINTON RAMEN', 'POPEYES', 'KFC', 'UBER EATS', 'SKIPTHEDISHES',
            'DOORDASH', 'TAGPUAN', 'BLACKHORN DINING', 'ORIENTAL CHOPSTICKS',
            'SZECHUAN EXPRESS', 'SOFRA NAZAR', 'DAMAS MEDITERRANEAN'
        ],
        'Transportation': [
            'PRESTO', 'UBER', 'UBER TRIP', 'UBER CANADA', 'PARKING'
        ],
        'Groceries': [
            'WALMART', 'WAL-MART', 'NOFRILLS', 'NO FRILL', 'METRO', 'LONGO',
            'HONG TAI SUPERMARKET', 'JIAN HING FOODMART', 'INSTACART',
            'ALI\'S NO FRILLS', 'RICHARD & RUTH\'S NF', 'PINOY MINI STORE'
        ],
        'Shopping': [
            'AMAZON', 'AMZN', 'BEST BUY', 'HOME DEPOT', 'SHOPPERS DRUG MART',
            'H & M', 'HM', 'URBAN', 'WINNERS', 'VANS', 'ALDO', 'MINISO',
            'DOLLARAMA', 'VALUE VILLAGE', 'ONCE UPON A CHILD', 'ARDENE',
            'BATH AND BODY WORKS', 'JOE FRESH'
        ],
        'Technology & Software': [
            'MICROSOFT', 'MSFT', 'OFFICE 365', 'HEROKU', 'DIGITALOCEAN',
            'ADOBE', 'VUESCHOOL', 'UDEMY', 'NAME.COM'
        ],
        'Entertainment & Subscriptions': [
            'NETFLIX', 'CRUNCHYROLL', 'SPOTIFY', 'ONLYFANS', 'YOUTUBE',
            'FAMOUS PLAYER', 'GOOGLE'
        ],
        'Health & Fitness': [
            'UPTOWN FITNESS', 'DR. TAVAKOLI', 'SCARBOROUGH HOSPITAL',
            'LAWRENCE PHARMACY', 'ECONOMICAL INSURANCE'
        ],
        'Travel': [
            'PAL AIR', 'PHILIPPINE AIRLINE', 'CHEAPOAIR', 'BAI HOTEL',
            'CITIZENSHIP & IMMIGRATION'
        ],
        'Fees & Interest': [
            'BALANCE PROTECTION', 'RETAIL INTEREST', 'CASH INTEREST'
        ],
        'Payments': [
            'PAYMENT - THANK YOU', 'REWARDS REDEMPTION'
        ],
        'Other Services': [
            'TELUS', 'EXPERT TAILOR', 'SKILLED TRADES COLLEGE', 'COINAMATIC'
        ]
    }
    
    def categorize_description(description):
        desc_upper = description.upper()
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.upper() in desc_upper:
                    return category
        return 'Other'
    
    df['Category'] = df['Description'].apply(categorize_description)
    return df

def analyze_spending_patterns(df):
    """Analyze spending patterns and trends"""
    
    print("\n=== SPENDING BY CATEGORY ===")
    spending_by_category = df[df['Amount'] > 0].groupby('Category')['Amount'].agg(['sum', 'count', 'mean']).round(2)
    spending_by_category = spending_by_category.sort_values('sum', ascending=False)
    
    for category, row in spending_by_category.iterrows():
        print(f"{category:<25}: ${row['sum']:>8.2f} ({row['count']:>3} transactions, avg: ${row['mean']:>6.2f})")
    
    print("\n=== YEARLY SPENDING TRENDS ===")
    yearly_spending = df[df['Amount'] > 0].groupby('Year')['Amount'].sum().round(2)
    for year, amount in yearly_spending.items():
        print(f"{year}: ${amount:,.2f}")
    
    print("\n=== MONTHLY SPENDING PATTERNS ===")
    monthly_avg = df[df['Amount'] > 0].groupby('MonthName')['Amount'].mean().round(2)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    for month in month_order:
        if month in monthly_avg.index:
            print(f"{month:<10}: ${monthly_avg[month]:>7.2f} average")
    
    return spending_by_category, yearly_spending, monthly_avg

def analyze_frequent_merchants(df):
    """Analyze most frequent merchants and spending patterns"""
    
    print("\n=== TOP MERCHANTS BY SPENDING ===")
    merchant_spending = df[df['Amount'] > 0].groupby('Description')['Amount'].agg(['sum', 'count']).round(2)
    merchant_spending = merchant_spending.sort_values('sum', ascending=False).head(15)
    
    for merchant, row in merchant_spending.iterrows():
        print(f"{merchant:<35}: ${row['sum']:>8.2f} ({row['count']:>2} visits)")
    
    print("\n=== MOST FREQUENT MERCHANTS ===")
    frequent_merchants = df[df['Amount'] > 0]['Description'].value_counts().head(15)
    
    for merchant, count in frequent_merchants.items():
        total_spent = df[(df['Description'] == merchant) & (df['Amount'] > 0)]['Amount'].sum()
        print(f"{merchant:<35}: {count:>3} visits (${total_spent:>8.2f} total)")

def payment_analysis(df):
    """Analyze payment patterns"""
    
    payments = df[df['Amount'] < 0]
    print(f"\n=== PAYMENT ANALYSIS ===")
    print(f"Total payments made: {len(payments)}")
    print(f"Total amount paid: ${abs(payments['Amount'].sum()):,.2f}")
    print(f"Average payment: ${abs(payments['Amount'].mean()):,.2f}")
    print(f"Largest payment: ${abs(payments['Amount'].min()):,.2f}")
    
    yearly_payments = payments.groupby('Year')['Amount'].agg(['count', 'sum']).round(2)
    yearly_payments['sum'] = abs(yearly_payments['sum'])
    
    print("\nPayments by year:")
    for year, row in yearly_payments.iterrows():
        print(f"{year}: {row['count']} payments, ${row['sum']:,.2f} total")

def main():
    """Main analysis function"""
    print("🏦 CREDIT CARD TRANSACTION ANALYSIS")
    print("=" * 50)
    
    # Load data
    df_all, yearly_stats = load_and_analyze_transactions()
    
    # Categorize transactions
    df_categorized = categorize_transactions(df_all)
    
    # Analyze spending patterns
    spending_by_category, yearly_spending, monthly_avg = analyze_spending_patterns(df_categorized)
    
    # Analyze merchants
    analyze_frequent_merchants(df_categorized)
    
    # Analyze payments
    payment_analysis(df_categorized)
    
    print("\n=== FINANCIAL INSIGHTS ===")
    print("• Most spending: Food & Dining, Groceries, Shopping")
    print("• Regular subscriptions: Netflix, Microsoft Office, Heroku")
    print("• Transportation: Consistent Presto card usage")
    print("• Payment behavior: Regular payments to manage credit balance")
    print("• Trend: Spending patterns show lifestyle changes over years")

if __name__ == "__main__":
    main()
