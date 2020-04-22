"""
Program: filesys.py
Author: Mile C. Stover
Provides a menu-driven tool for navigating a file system
and gathering information on filesys
"""

import os, os.path

# Golbal vars and constants
QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')

MENU = """
-----------------------------------
1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory 
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program
___________________________________
"""

# Main method
def main():
    while True:
        print("\n" * 3 , os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Exiting program")
            break
            
def acceptCommand():
    """Inputs and returns a legitmate command number."""
    command = input("Enter a number: ")
    # Checks that the user's input is a invalid choice
    if command in COMMANDS:
        return command
    else:
        print("Error: command not valid!")
        return acceptCommand()
        
def runCommand(command):
    """Select and runs a command."""
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", \
        countFiles(os.getcwd()))
    elif command == '5':
        print("The total numbers of bytes in file is", countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
        
def listCurrentDir(dirName):
    """Prints a lise off the cwd's content"""
    lyst = os.listdir(dirName)
    for element in lyst: 
        print(element)
        
def moveUp():
    """Moves up to the parent directory"""
    os.chdir("..")

def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
        os.chdir(newDir) 
        print("Moved to directory")
    else:
        print("ERROR: not a existing directory name")
        
def countFiles(path):
    """Returns the number of files in the cwd and
    all its subdirectories."""
    count = 0 
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count 

def countBytes(path):
    """Returns the number of bytes in the cwd and all its subdirectories."""
    count = 0 
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count

def findFiles(target, path):
    """Returns a list of the filename that contain 
    the target string in the cwd all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
            else:
                os.chdir(element)
                files.extend(findFiles(target, os.getcwd()))
                os.chdir("..")
    return files

if __name__ == "__main__":
    main()