#  Attendance Management System (AMS)

This repository contains the source code for a simple **Attendance Management System** implemented in Python. It is a console-based application that manages student records and attendance using local text files.

---

##  Project Details

| Field | Value |
| :--- | :--- |
| **Project Name** | **Attendance Management System (AMS)** |
| **Course** | Introduction to Problem Solving and Programing |
| **Submitted By** | Pari Pancholiya |
| **Registration Number** | 25BSA10049 |
| **Submitted To** | Dr. Vandana Shakya |
| **Institute** | VIT BHOPAl University |
| **Language** | **Python 3** |

---

##  Features

The system provides the following core functionalities:

1.  **Add Student Detail:** Register a new student by Roll Number and Name, ensuring the **Roll Number is unique**.
2.  **Mark Student Attendance:** Record attendance (Present 'P' or Absent 'A') for a student for the current date, ensuring **attendance is marked only once per day** per student.
3.  **View Student Details:** Display a list of all registered students (Roll Number and Name).
4.  **Generate Student Report:** Calculate and display the total days, present days, and overall **attendance percentage** for a specific student.
5.  **Exit:** Terminate the program.

---

##  Setup & Execution

### Prerequisites

* **Python 3.x**

### Pseudocode

1.  Save the provided code as a Python file (e.g., `attendance_system.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the Python interpreter:

    ```bash
    python attendance_system.py
    ```

### Interactive Menu

| Option | Description |
| :--- | :--- |
| **1** | **Add Student Detail** |
| **2** | **Mark Students Attendance** |
| **3** | **View Students Detail** |
| **4** | **Generate Students Report** |
| **5** | **Exit** |

---

##  Data Files

The system automatically creates two text files in the same directory upon first run. These files act as the persistent storage for the application:

| File Name | Purpose | Data Format (Comma-Separated) |
| :--- | :--- | :--- |
| `students.txt` | Stores permanent student details. | `RollNumber,StudentName` |
| `attendance.txt` | Stores daily attendance records. | `RollNumber,Date,Status` (Date is YYYY-MM-DD, Status is P or A) |

---

##  Code Documentation

### Dependencies

The script uses standard Python libraries:

* **`os`**: Used for checking file existence (`os.path.exists`).
* **`datetime`**: Used to capture the current date and time (`datetime.now().strftime("%Y-%m-%d")`) for attendance records.

### Functional Components

| Function Name | Description | Key Logic/Validation |
| :--- | :--- | :--- |
| **`markStudentAttendance()`** | Records a student's daily attendance. | Checks if attendance is **already marked for the current day**. |
| **`addStudentDetails()`** | Registers a new student's details. | **Prevents duplicate Roll Numbers** by checking existing records. |
| **`viewStudentDetails()`** | Displays the list of all registered students. | Reads and prints all records from `students.txt`. |
| **`showStudentReport()`** | Calculates and displays a student's attendance statistics. | Counts total days and present days, then calculates attendance **percentage** (e.g., $P = \frac{\text{presentDays}}{\text{totalDays}} \times 100$). |
| **`main()`** | The main execution loop of the system. | Displays the menu, handles user input, and calls the appropriate function. |

## Flowchart

+--------------------------+
|          START           |
+--------------------------+
             |
             v
+--------------------------+
| Initialize Files:        |
| students.txt             |
| attendance.txt           |
+--------------------------+
             |
             v
+--------------------------+
|      MAIN MENU LOOP      |
| Display Options (1-5)    |
+--------------------------+
             |
    +--------+--------+--------+--------+--------+
    |        |        |        |        |        |
    v        v        v        v        v        v
(Choice 1) (Choice 2) (Choice 3) (Choice 4) (Choice 5)
                                                 |
                                                 v
                                        +-------------------+
                                        |   EXIT PROGRAM    |
                                        +-------------------+

--- Flow for Choice 1: Add Student Detail ---
+--------------------------+
| Input Roll Number & Name |
+--------------------------+
             |
             v
+--------------------------+
| Check if Roll Number     |
| Exists in students.txt   |
+-------------+------------+
              |
      +-------+-------+
      |               |
      v               v
    (Yes)            (No)
+----------------+ +------------------------+
| Print "Roll No | | Append RollNo, Name to |
| already exists"| | students.txt           |
+----------------+ +------------------------+
      |               |
      v               v
+-----------------+ +----------------------+
| Return to Menu  | | Print "Student Added"|
+-----------------+ +----------------------+
                      |
                      v
                      (Return to Menu)

--- Flow for Choice 2: Mark Students Attendance ---
+---------------------------+
| Input Roll No & Status P/A|
| Get Current Date          |
+---------------------------+
             |
             v
+--------------------------+
| Check if attendance      |
| already marked for today |
+-------------+------------+
              |
      +-------+-------+
      |               |
      v               v
    (Yes)           (No)
+----------------+ +------------------------+
| Print "Cannot  | | Append RollNo, Date,   |
| mark twice"    | | Status to attendance.txt|
+----------------+ +------------------------+
      |               |
      v               v
+-----------------+ +---------------------+
| Return to Menu  | | Print "Attendance   |
+-----------------+ +---------------------+
                      | marked"
                      v
                  (Return to Menu)

--- Flow for Choice 3: View Students Detail ---
+--------------------------+
| Read students.txt        |
+-------------+------------+
              |
      +-------+-------+
      |               |
      v               v
 (Empty)           (Has Data)
+----------------+ +------------------------+
| Print "No      | | Print contents of      |
| records found" | | students.txt           |
+----------------+ +------------------------+
      |               |
      v               v
      (Return to Menu)

--- Flow for Choice 4: Generate Students Report ---
+--------------------------+
| Input Roll Number        |
+--------------------------+
             |
             v
+----------------------------+
| Loop through attendance.txt|
| Count totalDays and        |
| presentDays for Roll No    |
+-------------+--------------+
              |
      +-------+-------+
      |               |
      v               v
(totalDays == 0) (totalDays > 0)
+----------------+ +------------------------+
| Print "No       | | Calculate Percentage:  |
| records found" | | (present/total) * 100  |
+----------------+ +------------------------+
      |               |
      v               v
      |               |
      |               v
      |       +------------------------+
      |       | Print full Report      |
      |       | (Days & Percentage)    |
      |       +------------------------+
      |               |
      v               v
      (Return to Menu)
