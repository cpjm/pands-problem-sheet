students= []
def displayMenu():

    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()
    return choice

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

def doAdd(students):
    newStudent={}
    newStudent["name"] = input("Enter Student Name: ")
    newStudent["modules"] = modulesRead()
    students.append(newStudent)

def doView(students):
    for student in students:
        print (student["name"])
        for module in student["modules"]:
            print ("\t", module["name"], "\t:" , module["grade"], "\t")
    

def doSave(students):
    #you will put the call to save dict here
    savedict()
    
def savedict():
    writeDict(students)
    print("students saved")    
    
#main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
    choice=displayMenu()
