from backend.main import *

def main():
    connection = create_connection()
    if connection:
        create_todo_table(connection)
        
        while True:
            print("\n1. Add Todo\n2. View Todos\n3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                task = input("Enter the task: ")
                add_todo(connection, task)
            elif choice == "2":
                todos = get_todos(connection)
                if todos:
                    print("\nTodos:")
                    for todo in todos:
                        print(f"{todo[0]}. [{ 'x' if todo[2] else ' ' }] {todo[1]}")
                else:
                    print("No todos found.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

        connection.close()
        print("Exiting.")

if __name__ == "__main__":
    main()
