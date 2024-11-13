# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Renato Felicio,11/10/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # This variables will hold data read from file
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
import json # Imports code from Python's json module into script
try:
    file = open(FILE_NAME, "r") # Open the JSON file for reading
    students = json.load(file) # File data is loaded into a table
    # Now 'students' contains the parsed JSON data as a Python list of dictionaries
    file.close()
except FileNotFoundError as e:  # Handles error in case there is no initial file
    print("Data file must exist before running this script!\n")
    print(e, e.__doc__, type(e), sep='\n') # prints error message
    file = open(FILE_NAME, "w") # Creates an empty initial file, in case of file not found
    print("Empty file was created")
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally: # It closes the file
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try: # It handles user entering a non-alphabetic character for first name
            student_first_name = input("Enter the student's first name: ") # Asks user for student's first name
            if not student_first_name.isalpha(): # checks if student's first name is all alphabetic characters
                raise ValueError("Student's first name should contain only alphabetic characters.") # Custom error

        except ValueError as e: # Prints error message and restarts loop
            print(e, e.__doc__, type(e), sep='\n')  # Prints the custom message
            continue

        try:# It handles user entering a non-alphabetic character for last name
            student_last_name = input("Enter the student's last name: ")  # Asks user for student's last name
            if not student_last_name.isalpha(): # checks if student's last name is all alphabetic characters
                raise ValueError("Student's last name should contain only alphabetic characters.") # Custom error
        except ValueError as e:# Prints error message and restarts loop
            print(e, e.__doc__, type(e), sep='\n')  # Prints the custom message
            continue

        course_name = input("Please enter the name of the course: ")# Asks user for student's course name

        #User input data is loaded into a dictionary below:
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName":course_name}
        students.append(student_data) # Dictionary with user input data is appended to a table with all students\
                                      # information
    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        # Loops through dictionaries in the list and prints as a formated string
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file) # It writes the list of dictionaries into a json file
        except Exception as e: # It handles any exception that could happen when writing the file
            print("There was an error writing into the data file")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            print("Data File Closed")
            file.close()
        print("The following data was saved to file!\n")
        for student in students:
            json_data +=f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}\n"
        print(json_data)  # print formated string with all the data saved into json file
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
