# Student CLI System

A command-line based Student Management System built with Python that stores data using JSON persistence. This project allows users to manage student records through a modular backend-style architecture.

## Features

* User Registration and Login System
* Password Validation with Special Character Requirements
* Add Student Records
* Update Student Information
* Delete Student Records
* Search Student Records
* Display All Students
* Student Performance Analysis Report

  * Number of Passed Students
  * Number of Failed Students
  * Highest Grade
  * Lowest Grade
* JSON File Persistence

  * Data remains saved even after the program is closed

## Project Structure

* `main.py` — Program flow and menu navigation
* `auth.py` — User authentication and registration logic
* `student_service.py` — Student management functions (CRUD operations)
* `storage.py` — JSON file handling (load and save operations)
* `users.json` — User account storage
* `students.json` — Student record storage

## Concepts Demonstrated

* Python Functions
* Dictionaries
* Loops and Conditionals
* Input Validation
* JSON Persistence
* Modular Programming
* Multi-file Project Structure
* Separation of Concerns
* Backend Logic Design
* Debugging and Error Handling

## Technologies Used

* Python 3
* JSON


