# Simple Student System
# encoding:utf-8
import csv
import sys
import random
 
def selectCourses(courses):
    selection = False
    while selection == False:
        try:
            choise = int(input("How many courses do you want to choose? "))
            if choise > 5:
                print("Invalid, You can choose maximum of 5 courses!")
            elif choise < 3:
                print("You failed in class!")
                menu()
                break
            else:
                selection = True
                course = random.choice(courses)
                print(f"---Exam: {course} ---")
                getGrades()
                break
        except:
            print("This field can not be empty!")
            break


def getGrades():
    grades = {"midterm":None,"final":None,"project":None}
    while True:
        try:
            for key,value in grades.items():
                if grades[key] == None:
                    grades[key] = int(input(f"Please enter {key}: "))
            break
        except ValueError:
            print("Invalid")

    calculate(grades)
    return grades

def calculate(grades):
    print("----------------------------------")
    print("Your passing grade is calculating....")
    for k,v in grades.items():
        print(f"Your {k}: {v} ")
    
    result = (grades['midterm']*0.3) + (grades['final']*0.5) + (grades['project']*0.2)
    print("Result: ",result)

    if result >= 90:
        print("Letter Grade is AA")
        menu()
    elif 70 <= result < 90:
        print("Letter Grade is BB")
        menu()
    elif 50 <= result < 70:
        print("Letter Grade is CC")
        menu()
    elif 30 <= result < 50:
        print("Letter Grade is DD")
        menu()
    else:
        print("Letter Grade is FF")
        print("You failed in class!")
        menu()


def addCourse():
    courses = []
    while len(courses) < 5:
        course = input("Please enter the name of course: ")
        if not course:
            print("This field can not be empty!")
        elif course in courses:
            print("Already exist!")
        else:
            courses.append(course)
    for i in range(len(courses)):
        print(f"{i+1}.Course: {courses[i]}")
    
    selectCourses(courses)
    return courses

def login():
    count = 3
    filename="student.csv"
    users=[]
    print("----Student Management System----")
    with open(filename,'r') as data:
        for line in csv.DictReader(data):
            users.append(line)
        while count > 0:
            name = input("Please enter your name: ")
            surname = input("Please enter your surname: ")
            try: 
                check = next(user for user in users if user['Name'] == name and user['Surname'] == surname)
                print("----------------------------------")
                print(f"Successfully logged in, Welcome {name}")
                print("----------------------------------")
                break
            except:
                count -= 1
                print("Invalid name or surname")
                if count == 0:
                    print("Please, Try again later")
                    sys.exit()

def menu():
    choice = True
    print(""" --Main Menu--
    1. Add Course
    2. Exit """)
    choice = input()
    if choice == "1":
        addCourse()
    elif choice == "2":
        sys.exit()
    else:
        print("Not valid choice try again!!")

def main():
    login()
    menu()

if __name__ == "__main__":
    main()