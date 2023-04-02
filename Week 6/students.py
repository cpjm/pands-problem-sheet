# About: Week 6 weekly Task
# Author: Ciaran Moran
# Program name: students.py
# Desc: Program that will maintain a list of students
# 
#

students = []

def displayMenu():
    print("MENU")
    print("----")
    print ("")
    print ("\ta - Add")
    print ("\tv - View")
    print ("\tq - Quit")
    print ("")
    return str(input("Enter your choice: "))
    
def modulesRead():
    newModules = []

    newModuleName = input ("Please enter module name: ")
    while (newModuleName != ""):
        newModule = {}
        newModule["name"] = newModuleName
        newModule["grade"] = int(input ("Please enter a grade: "))
        newModules.append(newModule)  
    
        newModuleName = input ("Please enter module name: ")

    return newModules

def studentAdd(students):
    newStudent={}
    newStudent["name"] = input("Enter Student Name: ")
    newStudent["modules"] = modulesRead()
    students.append(newStudent)
    
    
def studentView(students):
    for student in students:
        print (student["name"])
        for module in student["modules"]:
            print ("\t", module["name"], "\t:" , module["grade"], "\t")
    
menuOption = displayMenu()
while menuOption != "q":
    if menuOption=="a" :
        studentAdd(students)
    elif menuOption=="v" :
        studentView(students)
    else:
        print ("Invalid Choice!")

    menuOption = displayMenu()
   
print("Goodbye!")
