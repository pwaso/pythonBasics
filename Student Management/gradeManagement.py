import sys

studentDatabase = {}
subjects = ['Computer Programming', 'Deriving Values']
options = [1, 2, 3, 4, 5]

print('Welcome to the Student Grade Management System!')


class InvalidGradeException(Exception):
    def __init__(self, message):
        super().__init__(message)


def validateGrade(grade):
    return grade < 0 or grade > 100


def checkStudentPresent(name):
    if name in studentDatabase:
        return True
    return False


def addStudent():
    name = input('Enter Student Name: ')
    grades = []
    for subject in subjects:
        while True:
            try:
                grade = int(input(f'Enter Grade of {subject}: '))
                if validateGrade(grade):
                    raise InvalidGradeException("Invalid Grade!")
                grades.append(grade)
                break
            except (ValueError, InvalidGradeException) as e:
                print(e)
    studentDatabase[name] = grades
    print("Student Added Successfully!")


def displayStudents():
    for key, value in studentDatabase.items():
        print(f'{key}: {value}')


def calculateAverage():
    for key, value in studentDatabase.items():
        average = sum(value) / len(value)
        print(f'{key}: {average}')


def updateStudents():
    name = input('Enter Student Name: ')
    if checkStudentPresent(name):
        grades = []
        for subject in subjects:
            while True:
                try:
                    grade = int(input(f'Enter Grade of {subject} for {name}: '))
                    if validateGrade(grade):
                        raise InvalidGradeException("Invalid Grade!")
                    grades.append(grade)
                    studentDatabase[name] = grades
                    break
                except (ValueError, InvalidGradeException) as e:
                    print(e)
    else:
        print("Student Not Found!")


while True:
    print('\n1. Add Student\n2. Update Grade\n3. Display Grades\n4. Calculate Average\n5. Exit')
    try:
        option = int(input('Enter your choice: '))
        if option == 1:
            addStudent()
        elif option == 2:
            updateStudents()
        elif option == 3:
            displayStudents()
        elif option == 4:
            calculateAverage()
        elif option == 5:
            sys.exit()
        else:
            print('Invalid option!')
    except ValueError:
        print('Please enter valid option!')
