-- Initialize the financial tracker database
-- This script runs when the PostgreSQL container starts for the first time

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    user_id uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(500) NOT NULL UNIQUE,
    user_password VARCHAR(250) NOT NULL,
    user_settings jsonb NOT NULL DEFAULT '{}',
    user_notes jsonb NOT NULL DEFAULT '{}',
    user_activity jsonb NOT NULL DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create statement table (fix the typo in column name)
CREATE TABLE IF NOT EXISTS statement (
    id uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    date date NOT NULL,
    description TEXT NOT NULL,
    statement_type VARCHAR(250) NOT NULL,
    withdrawn_amount MONEY NOT NULL DEFAULT '$0.00',
    deposited_amount MONEY NOT NULL DEFAULT '$0.00',
    balance_amount MONEY NOT NULL DEFAULT '$0.00',
    transaction_purpose VARCHAR(250) NOT NULL DEFAULT 'other',
    statement_owner uuid REFERENCES users(user_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_statement_date ON statement(date);
CREATE INDEX IF NOT EXISTS idx_statement_type ON statement(statement_type);
CREATE INDEX IF NOT EXISTS idx_statement_owner ON statement(statement_owner);
CREATE INDEX IF NOT EXISTS idx_statement_purpose ON statement(transaction_purpose);

-- Create a default user for development
INSERT INTO users (email, user_password, user_settings, user_notes, user_activity)
VALUES (
    'demo@financialtracker.com',
    'demo123',
    '{"theme": "dark", "currency": "USD"}',
    '{"welcome": "Welcome to your financial tracker!"}',
    '{"last_login": "2025-09-06"}'
) ON CONFLICT (email) DO NOTHING;

-- Create a function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers to auto-update timestamps
DROP TRIGGER IF EXISTS update_users_updated_at ON users;
CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_statement_updated_at ON statement;
CREATE TRIGGER update_statement_updated_at
    BEFORE UPDATE ON statement
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE money TO postgres;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO postgres;
