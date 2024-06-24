import sqlite3
from tabulate import tabulate

# Initialize the database and create the table
def init_db():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users')  # Drop the existing table if it exists
    cur.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            salary INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Create a new user
def create_user(name, age, salary):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, age, salary) VALUES (?, ?, ?)', (name, age, salary))
    conn.commit()
    conn.close()

# Read all users
def read_users():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    conn.close()
    return users

# Update an existing user
def update_user(user_id, name, age, salary):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = ?, age = ?, salary = ? WHERE id = ?', (name, age, salary, user_id))
    conn.commit()
    conn.close()

# Delete a user
def delete_user(user_id):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

# Display the menu and handle user input
def display_menu():
    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = int(input('Enter salary: '))
            create_user(name, age, salary)
            print(f"User {name} added.")
        elif choice == '2':
            users = read_users()
            print("Users:")
            headers = ["ID", "Name", "Age", "Salary"]
            print(tabulate(users, headers, tablefmt="grid"))
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            salary = int(input("Enter new salary: "))
            update_user(user_id, name, age, salary)
            print(f"User {user_id} updated.")
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
            print(f"User {user_id} deleted.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize the database
init_db()

# Display the menu
display_menu()
