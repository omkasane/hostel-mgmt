import sqlite3

def create_tables():
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    
    # Create Students Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        room_id INTEGER,
        FOREIGN KEY (room_id) REFERENCES rooms (room_id)
    )
    ''')
    
    # Create Rooms Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        room_id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_number TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        current_occupants INTEGER DEFAULT 0
    )
    ''')
    
    # Create Payments Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        amount REAL,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students (student_id)
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
