
import psycopg2
from getpass import getpass

def create_connection():
    try:
        connection = psycopg2.connect(
            user=input("Enter PostgreSQL username: "),
            password=getpass("Enter PostgreSQL password: "),
            host="localhost",
            port="5432",
            database="tododb",
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_todo_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL
            );
        """)
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Error creating table: {e}")

def add_todo(connection, task):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO todos (task, completed) VALUES (%s, %s);", (task, False))
        connection.commit()
        cursor.close()
        print("Task added successfully.")
    except Exception as e:
        print(f"Error adding task: {e}")

def get_todos(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM todos ORDER BY id;")
        todos = cursor.fetchall()
        cursor.close()
        return todos
    except Exception as e:
        print(f"Error retrieving todos: {e}")
        return []

