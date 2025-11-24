# 📘 Attendance Management System  
A simple menu-driven Python project to record student details, mark attendance, and generate attendance reports.  
Beginner-friendly and suitable for 1st-semester project submission.

---

## 🚀 Project Objective
The objective of this project is to create a basic attendance system that:
- Stores student information
- Records daily attendance
- Generates attendance summary reports
- Demonstrates file handling, functions, and modular programming

---

## 📂 Features (Functional Requirements)
### ✔ 1. Student Management
- Add student name and roll number  
- Prevent duplicate roll numbers  
- View the student list  

### ✔ 2. Attendance Recording
- Mark Present (P) or Absent (A)
- Automatically stores date
- Prevent duplicate attendance for same day

### ✔ 3. Attendance Report
- Show total days recorded
- Count present days
- Calculate attendance percentage

---

## 🛠 Non-Functional Requirements
- **Usability:** Easy menu interface  
- **Reliability:** Validates roll numbers and duplicate entries  
- **Maintainability:** Modular functions  
- **Error Handling:** Handles blank files, invalid input  
- **Performance:** Fast file-based system  
- **Scalability:** New features can be added easily  

---

## 🧩 System Flowchart (Mermaid)

```mermaid
flowchart TD

A[Start] --> B[Main Menu]

B --> C{Choose Option}

C -->|1. Add Student| D[Enter Roll No & Name]
D --> E[Save to students.txt]
E --> B

C -->|2. Mark Attendance| F[Enter Roll No]
F --> G[Check if Roll Exists]
G -->|Yes| H[Save Attendance with Timestamp]
G -->|No| I[Show Error: Student Not Found]
H --> B
I --> B

C -->|3. View Students| J[Read students.txt]
J --> B

C -->|4. View Attendance| K[Read attendance.txt]
K --> B

C -->|5. Exit| L[End]        
