
# About: Week 7 weekly Task
# Author: Ciaran Moran
# Program name: es.py
# Desc: Program that will take a filename from the command line, 
# open the file, and count the number of "e" characters.
# 
import sys
import os

def countEs (filename=""):
    cnt = 0
    if (filename!="" and os.path.exists(filename)) :
        # open the file and count the 'e's within
        f = open(filename, "r")
        fileLines = f.readlines()
        for fileline in fileLines :
            cnt+=fileline.count("e")
        f.close()      
    return cnt
    
# Discovered by using a print display that 
# sys.argv[0] is actually the name of the script being run
# e.g. es.py
# So the first arg is actually  sys.argv[1]
# The first arguement passed is sys.argv[2], and so on.
#
# Lets check the count of command line arguements passed
argCount = len(sys.argv)
# if >1 then yes an aguement was passed
if argCount > 1 :
    #okay to set as there is an arguement passed from command line
    FILENAME = sys.argv[1]

    #now call function to count the 'e's in the file
    ans = countEs(FILENAME)

    #now output the results of count of 'e's found
    if ans == 0 :
        print ("There are no 'e's in the file ", FILENAME)
    elif ans==1 :
       print ("There is 1 'e'' in the file", FILENAME)
    else :
       print ("There are" , ans, "'e's in the file", FILENAME)   
else:
    # no command line arguement passed
    print ("Error, command line arguement cannot be blank ")
    