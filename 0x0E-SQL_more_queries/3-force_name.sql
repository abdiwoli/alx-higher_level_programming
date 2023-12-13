-- Create the table force_name if it doesn't exist
-- Check if the table exists before creating it
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
