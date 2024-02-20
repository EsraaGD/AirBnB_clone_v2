-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user and set the password
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
