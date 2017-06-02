student_list = []

def create_student():
    user_name = input("Enter student Name: ")
    student_data = {
        'name': user_name,
        'marks': []
    }
    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number


def student_details(student):
    print("{}, average mark: {}.".format(student['name'], calculate_average_mark(student)))


def print_student_details(students):
    for i, student in enumerate(students):
        print("ID:{}".format(i))
        student_details(student)


def menu():
    selection = input("Enter 'p' to print the student list," "'s' to add a new student,"
                      " 'a' to add a mark to a student," "or 'q' to quit.")
    while selection != 'q':
        if selection == 'p':
            print_student_details(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter a student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)

        selection = input("Enter 'p' to print the student list," "'s' to add a new student,"
                          " 'a' to add a mark to a student," "or 'q' to quit.")

menu()