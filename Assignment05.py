# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DPetkov,4.27.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
# dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have in a text file
# called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

myFile = open(objFile, "a")  # Opening append mode
dicRow = {"task": "TASK", "priority": "PRIORITY"}
myFile.write(dicRow["task"] + '|' + dicRow["priority"] + '\n')  # Write column headers to file
myFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):

        print("This is the current data in the file:\n")
        myFile = open(objFile, "r")  # Open file for reading
        for row in myFile:  # For every row in the file
            lstTable = row.split("|")  # Returns a list with the variables split by |
            dicRow = {"task": lstTable[0], "priority": lstTable[1].strip()}  # List elements added to dictionary values
            print(dicRow)
        myFile.close()
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        # Get user input and add it to dictionary values
        TASK = input('Enter a task:')
        PRIORITY = input('Enter a priority:')
        dicRow = {"task": TASK, "priority": PRIORITY}
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        # Open file in read and write
        myFile = open(objFile, "r+")
        lines = myFile.readlines()  # Read every line in the file and add it to a list
        REMOVE = int(input('Enter the desired row you want to remove:')) - 1  # User selects what row they want deleted
        myFile.seek(0)  # Set pointer to 0
        myFile.truncate()  # Truncate
        for number, strData in enumerate(strData):  # Enumerate every line on the list
            if number not in [REMOVE]:  # Erase a line number equal to REMOVE
                myFile.write(strData)  # Write new data to file
        # Below is code recycled from option 1
        print("Your have altered your data, this is the current data:\n")
        myFile = open(objFile, "r")
        for row in myFile:
            lstRow = row.split("|")
            dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
            print(dicRow)
        myFile.close()
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):

        myFile = open(objFile, "a")  # Open file in append mode
        myFile.write(dicRow["task"] + '|' + dicRow["priority"] + '\n')  # Write values to the file
        print('You have saved', dicRow, 'to your file')  # Show user what they have added to file
        myFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('You are exiting the program, goodbye!')
        break  # and Exit the program
    # Step 8 - Invalid input
    else:
        print('---INVALID INPUT! PLEASE TRY AGAIN---')
