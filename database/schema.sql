CREATE TABLE covid19_data (
    id SERIAL PRIMARY KEY,
    province VARCHAR(100),
    country VARCHAR(100),
    date DATE,
    cases INTEGER
);
