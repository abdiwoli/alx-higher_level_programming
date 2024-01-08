-- Create or update user_0d_1 with all privileges

-- Connect to MySQL server with a user that has administrative privileges
-- You might need to replace 'root' and 'password' with your actual MySQL admin username and password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- If the server version is MySQL 5.7.6 or newer, you can use the following line instead
-- GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
