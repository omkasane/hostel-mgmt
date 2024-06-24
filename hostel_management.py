import sqlite3

def add_student(name, age, gender, room_id=None):
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (name, age, gender, room_id)
    VALUES (?, ?, ?, ?)
    ''', (name, age, gender, room_id))
    conn.commit()
    conn.close()

def assign_room(student_id, room_id):
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT capacity, current_occupants FROM rooms WHERE room_id=?', (room_id,))
    room = cursor.fetchone()
    if room and room[1] < room[0]:
        cursor.execute('UPDATE students SET room_id=? WHERE student_id=?', (room_id, student_id))
        cursor.execute('UPDATE rooms SET current_occupants = current_occupants + 1 WHERE room_id=?', (room_id,))
        conn.commit()
    else:
        print("Room is full or does not exist")
    conn.close()

def record_payment(student_id, amount, date):
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO payments (student_id, amount, date)
    VALUES (?, ?, ?)
    ''', (student_id, amount, date))
    conn.commit()
    conn.close()

def get_student(student_id):
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE student_id=?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

def get_all_students():
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

def get_room(room_id):
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms WHERE room_id=?', (room_id,))
    room = cursor.fetchone()
    conn.close()
    return room

def get_all_rooms():
    conn = sqlite3.connect('hostel_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms')
    rooms = cursor.fetchall()
    conn.close()
    return rooms

if __name__ == '__main__':
    # Example usage
    add_student('John Doe', 20, 'Male')
    add_student('Jane Smith', 21, 'Female')
    assign_room(1, 1)
    record_payment(1, 500.00, '2024-06-07')
    print(get_student(1))
    print(get_all_students())
    print(get_room(1))
    print(get_all_rooms())
