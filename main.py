from hostel_management import *

def main():
    while True:
        print("\nHostel Management System")
        print("1. Add Student")
        print("2. Assign Room")
        print("3. Record Payment")
        print("4. View Student")
        print("5. View All Students")
        print("6. View Room")
        print("7. View All Rooms")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            add_student(name, age, gender)
        
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            room_id = int(input("Enter room ID: "))
            assign_room(student_id, room_id)
        
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            record_payment(student_id, amount, date)
        
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            student = get_student(student_id)
            print(student)
        
        elif choice == '5':
            students = get_all_students()
            for student in students:
                print(student)
        
        elif choice == '6':
            room_id = int(input("Enter room ID: "))
            room = get_room(room_id)
            print(room)
        
        elif choice == '7':
            rooms = get_all_rooms()
            for room in rooms:
                print(room)
        
        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
