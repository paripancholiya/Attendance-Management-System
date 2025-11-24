import os
from datetime import datetime

studentDetails = "students.txt"
attendanceDetails = "attendance.txt"

# Create student and attendance file if not already present
if not os.path.exists(studentDetails):
    open(studentDetails, "w").close()

if not os.path.exists(attendanceDetails):
    open(attendanceDetails, "w").close()

# Function to mark student attendance
def markStudentAttendance():
    rollNumber = input("Enter students Roll Number - ")
    status = input("Enter P for Present or A for Absent -").upper()

    # getting date 
    date = datetime.now().strftime("%Y-%m-%d")

    # Attendance allowed only once a day for a student
    with open(attendanceDetails, "r") as file:
        for line in file:
            rollNo, dates, attendanceStatus = line.strip().split(",")
            if rollNo == rollNumber and dates == date:
                print("Attendance can only be marked once a day")
                return

    with open(attendanceDetails, "a") as file:
        file.write(f"{rollNumber},{date},{status}\n")
    print("Attendance marked.\n")

# Function to add student name and Roll number
def addStudentDetails():
    rollNumber = input("Enter Student's Roll Number - ")
    studentName = input("Enter Student's Name - ")

    # Duplicate roll number not allowed
    with open(studentDetails, "r") as file:
        for line in file:
            if line.startswith(rollNumber + ","):
                print("Roll number already exists")
                return

    with open(studentDetails, "a") as file:
        file.write(f"{rollNumber},{studentName}\n")
    print("Student is successfully Added\n")

# Function to view student details
def viewStudentDetails():
    print("\n List of Student")
    with open(studentDetails, "r") as file:
        fileContent = file.read()
        if fileContent.strip() == "":
            print("No students record found\n")
        else:
            print(fileContent)

# Function to Show Student Report
def showStudentReport():
    rollNumber = input("Enter Student's Roll Number - ")
    totalDays = 0 
    presentDays = 0

    with open(attendanceDetails, "r") as file:
        for line in file:
            rollNo, date, attendanceStatus = line.strip().split(",")
            if rollNo == rollNumber:
                totalDays += 1
                if attendanceStatus == "P":
                    presentDays += 1

    if totalDays == 0:
        print("No student records found")
        return
    # Cal present percent
    percentage = (presentDays / totalDays) * 100
    # Printing students attendance details
    print(f"Total number of Days: {totalDays}")
    print(f"Number of days student was Present: {presentDays}")
    print(f"Student's Attendance %: {percentage:.2f}\n")

def main():
    while True:
        print("Attendance Management System")
        print("1 - Add Student Detail")
        print("2 - Mark Students Attendance")
        print("3 - View Students Detail")
        print("4 - Generate Students Report")
        print("5 - Exit")

        userInputChoice = input("Kindly enter your choice - ")

        if userInputChoice == "1":
            addStudentDetails()
        elif userInputChoice == "2":
            markStudentAttendance()
        elif userInputChoice == "3":
            viewStudentDetails()
        elif userInputChoice == "4":
            showStudentReport()
        elif userInputChoice == "5":
            break
        else:
            print("Enter number only between 1-5")

main()