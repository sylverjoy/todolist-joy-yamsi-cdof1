
-- Create a 'todos' table
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL,
    completed BOOLEAN NOT NULL
);

-- Insert sample data
INSERT INTO todos (task, completed) VALUES
    ('Task 1', false),
    ('Task 2', true),
    ('Task 3', false);
