CREATE TABLE IF NOT EXISTS apartments (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    images TEXT[] NOT NULL
);