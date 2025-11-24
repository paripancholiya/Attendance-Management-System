# 5.2 statement.md: Attendance Management System (AMS)

---

## 1. Problem Statement

Manually tracking and calculating student attendance is **time-consuming, prone to errors**, and inefficient, especially when generating periodic reports or verifying daily presence. The lack of a simple, automated system makes it difficult for administrators or instructors to quickly retrieve attendance history, ensure data integrity (e.g., preventing duplicate entries), and accurately calculate a student's final attendance percentage.

---

## 2. Scope of the Project

The scope of this project is to create a **basic, console-based Attendance Management System (AMS)** using Python and file I/O operations (`.txt` files) for data persistence.

### In Scope:
* Storing student details (Roll Number and Name) in `students.txt`.
* Storing daily attendance records (Roll Number, Date, Status) in `attendance.txt`.
* Implementing data integrity checks to prevent duplicate Roll Numbers and duplicate daily attendance marks.
* Generating a report that calculates and displays a student's attendance percentage.

### Out of Scope:
* Using external databases (e.g., SQLite, MySQL).
* Developing a Graphical User Interface (GUI) or web interface.
* Advanced features like data security, user authentication, or bulk data import/export.
* Handling exceptions for date formats or non-numeric inputs (basic input validation is assumed).

---

## 3. Target Users

The primary target users for this system are individuals responsible for tracking and managing student presence.

* **Instructors/Teachers:** To quickly mark daily attendance and view individual student reports.
* **School/Department Administrators:** To maintain a basic record of attendance for a small class or group.
* **Students (Self-Use/Testing):** To check their own attendance record and percentage.

---

## 4. High-Level Features

The AMS is designed around four core operations accessible via a simple main menu:

| Feature | Description | Validation/Constraint |
| :--- | :--- | :--- |
| **Add Student Detail** | Register a new student's unique Roll Number and Name. | Ensures **Roll Number is not duplicated**. |
| **Mark Attendance** | Record a student's presence ('P') or absence ('A') for the current day. | Ensures **only one entry** is recorded per student per calendar day. |
| **View Student Details** | Display the list of all registered student records. | Retrieves and prints all data from `students.txt`. |
| **Generate Report** | Provide a summary report for a specific student. | Calculates and displays the **attendance percentage**. |