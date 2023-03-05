# About: Week 4 weekly Task
# Author: Ciaran Moran
# Program name: collatz.py
# Desc: Program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
#

#set some variables
inpN = int(input("\nPlease enter a positive integer: ")) # ask and get user input
wrkN = int(inpN) # working number
wrkS = "" # working string

if (inpN >= 1):
    validInp = True # boolean used to determine valid/invalid user input
else:
    validInp = False # boolean used to determine valid/invalid user input

while (wrkN > 1):
    # here we string together the resulting numbers in the loop
    wrkS = wrkS + " " + '{0:g}'.format(wrkN) # this formatting removes the ".0" as found on https://stackoverflow.com/questions/385325/dropping-trailing-0-from-floats
    if (wrkN % 2) == 0: # even number
        wrkN = wrkN / 2
    else: # odd number
        wrkN = (wrkN * 3) + 1
        
if validInp :
    wrkS = wrkS + " " + '{0:g}'.format(wrkN) # add the final number which will always be "1"
    print ("\nResult is:- " , wrkS) # output the results
else:
    print ("\nYou need to enter a valid integer!") # user didn't enter a positive integer
    