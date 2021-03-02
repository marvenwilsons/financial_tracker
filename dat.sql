CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    user_id uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(500) NOT NULL,
    user_password VARCHAR(250) NOT NULL,
    user_settings jsonb NOT NULL,
    user_notes jsonb NOT NULL,
    user_activity jsonb NOT NULL
);

CREATE TABLE statement (
    id uuid NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    date date NOT NULL,
    description TEXT NOT NULL,
    statement_type VARCHAR(250) NOT NULL,
    widthdrawn_amount MONEY NOT NULL,
    deposited_amount MONEY NOT NULL,
    balance_amount MONEY NOT NULL,
    transaction_purpose VARCHAR(250) NOT NULL,
    statement_owner TEXT NOT NULL REFERENCES users(user_id)
);
