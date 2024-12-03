# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Jason Coult, 11/29/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json # Load this library of functions so we can manipulate .json files

# Define constants
#Menu display
MENU: str = ''' 
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json" #Data file name

# Define the variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # dictionary of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try: #Try to open the file
    file = open(FILE_NAME,"r")
    students = json.load(file) #if this breaks, the codee will not reach the next line
    file.close() #use "finally" at end to close out file if this line not reached
except FileNotFoundError as e: #specific exception for file not found
    print("This specific .json file,", FILE_NAME,", was not found!\n")
    print("Here are the details of the error: ")
    print(e, e.__doc__, type(e), sep='\n') #access doc, show type, add newline
except Exception as e: #general catch-all exception if the error was something else
    print("There was a general error!\n") #indicate generic other error
    print("Here are the error details: ")  #show details
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False: #have to check if the file didn't close
        file.close() #and then close it out


# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        #Enclose in try-except to catch user input errors on first and last names
        try: #Obtain user input within this try block

            #Enter first name and check value for error
            student_first_name = input("Enter the student's first name: ") #individual data entry
            if len(student_first_name) == 0: #check for an empty entry first
                raise ValueError("The student's first name should not be empty.")
            elif not student_first_name.isalpha(): #then check if it contains numbers
                raise ValueError("The student's first name should not contain a number.")

            # Enter last name and check value for error
            student_last_name = input("Enter the student's last name: ")
            if len(student_last_name) == 0: #check for an empty entry first
                raise ValueError("The student's last name should not be empty.")
            elif not student_last_name.isalpha(): #then check if it contains numbers
                raise ValueError("The student's last name should not contain a number.")

            course_name = input("Please enter the name of the course: ")
            student_data = {"CourseName": course_name,  # add dictionary entry for single student
                            "FirstName": student_first_name,
                            "LastName": student_last_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue

        except ValueError as e: #Catching a specific value-type error
            print("-" * 50)
            print("There was a known error in the value of the student's name.") #Specific message about error
            print(e) #Print error-specific message
            print("Error details: ")
            print(e.__doc__,type(e), sep='\n')
            print("-" * 50)

        except Exception as e: #Catch-all for nonspecific error
            print("-" * 50)
            print("There was an unknown error when obtaining student name.") #Information about error
            print("Technical details of error: ") #Show details
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 50)


    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students: #loop through each dictionary entry/row
            #display each component of the individual row using the key names
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")

        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w") #open file in write mode
            json.dump(students, file) #write the students variable to the .json file
            file.close() #close out file

            #Now display the data, if the file operation worked
            print("-" * 50)
            print("Data saved successfully! This is the data saved: ")
            for student in students:
                # display each component of the individual row using the key names
                print(f"Student: {student["FirstName"]} {student["LastName"]}, Course: {student["CourseName"]}")
            print("-" * 50)
            continue

        except TypeError as e: #if it didn't work due to type error
            print("-" * 50)
            print("Please check the data is a valid json format\n")
            print("Technical details of error: ")
            print(e, e.__doc__, type(e), sep="\n")
            print("-" * 50)

        except Exception as e: #if it didnt work for another catch-all reason
            print("-" * 50)
            print("A general error has occurred when writing data to file.")
            print("General error information below: ")
            print(e, e.__doc__, type(e), sep="\n")
            print("-" * 50)

        finally: #then, if there was an error in first block and the file close never was reached
            if file.closed == False: #check for this
                file.close() #then close the file if it wasn't closed due to error in dump

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    #In case user did not select a valid choice
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended") #After loop exits, display this


