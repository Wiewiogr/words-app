CREATE DATABASE IF NOT EXISTS test_db;
use test_db;

CREATE TABLE movie (
    id INT NOT NULL auto_increment PRIMARY KEY,
    title VARCHAR(100),
    year INT,
    poster_url VARCHAR(200)
);

CREATE TABLE word (
    id INT NOT NULL auto_increment PRIMARY KEY,
    content VARCHAR(30),
    meaning TEXT
);

CREATE TABLE movie_word (
    movie_id INTEGER NOT NULL,
    word_id INTEGER NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movie (id) ON DELETE RESTRICT,
    FOREIGN KEY (word_id) REFERENCES word (id) ON DELETE RESTRICT,
    PRIMARY KEY (movie_id, word_id)
);