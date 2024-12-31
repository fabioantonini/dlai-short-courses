import sqlite3

# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')  # Creates a file named 'example.db'

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

# Insert data into the table
cursor.execute('''
INSERT INTO students (name, age, grade)
VALUES ('Alice', 21, 'A')
''')
cursor.execute('''
INSERT INTO students (name, age, grade)
VALUES ('Bob', 22, 'B')
''')

# Commit the changes
conn.commit()

# Query the database
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()