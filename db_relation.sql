-- SELECT version() -> PostgreSQL 14.10
DROP DATABASE cinema WITH (FORCE); 
CREATE DATABASE cinema;

CREATE TABLE IF NOT EXISTS films (
    title VARCHAR(50) NOT NULL, 
    genre VARCHAR(30) NOT NULL, 
    "year" INT NOT NULL,
    PRIMARY KEY(title)
);

CREATE TABLE IF NOT EXISTS actors (
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(50) NOT NULL, 
    film_title VARCHAR(30) NOT NULL, 
    PRIMARY KEY(id),
    FOREIGN KEY(film_title) REFERENCES films(title)
);

INSERT INTO films (title ,genre , "year")
VALUES ('Forest Gump', 'Drama', 1994);

SELECT * FROM films; 

INSERT INTO actors (name,film_title)
VALUES ('Tom Hanks', 'Forest Gump');

SELECT * FROM actors; 
