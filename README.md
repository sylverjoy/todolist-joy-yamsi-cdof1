# todolist-joy-yamsi-td1
A console based application to help keep track of tasks. You can add, delete and mark task completed.

# Command-Line Todo List App with PostgreSQL

This is a simple command-line-based to-do list application written in Python, with PostgreSQL as the backend database. The application allows you to add tasks, view tasks, and mark tasks as completed.

## Prerequisites

Before running this application, ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Python](https://www.python.org/downloads/)

## Set up PostgreSQL Docker Container

1. Clone this repository:

    ```bash
    git clone https://github.com/sylverjoy/todolist-joy-yamsi-cdof1.git
    cd todolist-joy-yamsi-cdof1
    ```

2. Build and run the PostgreSQL container:

    ```bash
    docker-compose up -d
    ```

## Running the Todo List App

1. Install the required Python packages:

    ```bash
    pip install psycopg2-binary
    ```

2. Run the Python script for the backend:

    ```bash
    python main.py
    ```

3. Follow the prompts to add tasks, view tasks, and exit the application.


## Additional Notes

- The PostgreSQL container is configured with a default username (`myuser`), password (`mypassword`), and database name (`tododb`). You can modify these in the Dockerfile and the Python script if needed.

- The `init.sql` file initializes the database with some sample tasks. You can modify this file to add or remove initial data.

- If you encounter any issues or have suggestions for improvement, feel free to open an issue or contribute to the project.

Happy task managing!

