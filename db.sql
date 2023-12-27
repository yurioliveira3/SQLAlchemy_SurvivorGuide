-- SELECT version() -> PostgreSQL 14.10 
CREATE DATABASE cinema;

CREATE TABLE IF NOT EXISTS films (
    title VARCHAR(50) NOT NULL, 
    genre VARCHAR(30) NOT NULL, 
    "year" INT NOT NULL,
    PRIMARY KEY(title)
);

INSERT INTO films (title,genre, "year")
VALUES('Forest Gump', 'Drama', 1994);

SELECT * FROM films;

INSERT INTO films (title,genre, "year")
VALUES('Scarface', 'Ação', 1983);