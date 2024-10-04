<?php

/*
Remember to replace your_username, your_password, and your_database with your actual database credentials. This code creates two tables, authors and books, with a one-to-many relationship between them using the author_id foreign key in the books table referencing the author_id primary key in the authors table.*/

// Database connection
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL queries to create tables
$createAuthorTable = "CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(50) NOT NULL
)";

$createBookTable = "CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_title VARCHAR(100) NOT NULL,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
)";

// Execute queries
if ($conn->query($createAuthorTable) === TRUE && $conn->query($createBookTable) === TRUE) {
    echo "Tables created successfully";
} else {
    echo "Error creating tables: " . $conn->error;
}

$conn->close();
?>
 
