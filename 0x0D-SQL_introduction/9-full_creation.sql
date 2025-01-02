-- displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO second_table (id, name, score)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);