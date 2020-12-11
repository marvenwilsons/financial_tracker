CREATE TABLE statement (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    date date NOT NULL,
    description TEXT NOT NULL,
    statement_type VARCHAR(250) NOT NULL,
    widthdrawn_amount MONEY NOT NULL,
    deposited_amount MONEY NOT NULL,
    balance_amount MONEY NOT NULL,
    transaction_purpose VARCHAR(250) NOT NULL
);

INSERT INTO statement (date,         description,       widthdrawn_amount, deposited_amount, statement_type, transaction_purpose, balance_amount) VALUES                                 19:23:24
(to_date('10-08-2020','MM-DD-YYYY'), 'PRESTO',              20.00, 0, 1,    essential,         4099.74),
(to_date('10-08-2020','MM-DD-YYYY'), 'DOLLARAMA  ',         12.15, 0, 1,    food-essential,    4111.89),
(to_date('10-08-2020','MM-DD-YYYY'), 'NICK  MIRAS NO FRILL',11.66, 0, 1,    Investment,        4123.55)


CREATE TABLE statement_type (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    type_name VARCHAR(255) NOT NULL
);

INSERT INTO statement_type (type_name) VALUES ('debit statement');