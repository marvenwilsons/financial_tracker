CREATE TABLE statement (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    date date NOT NULL,
    description TEXT NOT NULL,
    statement_type BIGINT NOT NULL  REFERENCES statement_type(id),
    statement_type VARCHAR(100) NOT NULL,
    widthdrawn_amount MONEY NOT NULL,
    deposited_amount MONEY NOT NULL,
    balance_amount MONEY NOT NULL
);

INSERT INTO statement 
    (date, description, widthdrawn_amount, deposited_amount, balance_amount, statement_type) VALUES
    (11/03/2020, 'PAYMENT - THANK YOU, 0)', 300.00, 4122.74),
    (11/03/2020, 'OLD NAVY CANADA 5488', 33.59, 0, 4156.33)


CREATE TABLE statement_type (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    type_name VARCHAR(255) NOT NULL
);

INSERT INTO statement_type (type_name) VALUES ('debit statement');