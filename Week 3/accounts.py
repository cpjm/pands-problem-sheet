# accounts.py
# Author: Ciaran Moran
# 

#Assuming that spaces are invalid and should be removed for length check
#Assuming that non-numeric input is invalid
#Assuming that input longer than 10 is invalid
#Assumming that input less than 10 in length is valid and will be right justified using zeros to the left
#

# A lot of time spent here via Google and Stackoverflow!
# Also the result of many many changes during trial runs...doh!
userEntryValid = False  # initialise before while loop
while (userEntryValid==False):
    bankAccount = str(input("Please enter a 10 digit account number (or x to exit): " ))

    # remove any spaces
    bankAccount = bankAccount.replace(" ","") 
    # print(f"1>> Bank Account entered is: {bankAccount}")
 
    if bankAccount=='X' or bankAccount=='x': 
        # Exit while loop. "break" found via Google
        # print(f"2>> Bank Account entered is: {bankAccount}")
        break 
    
    # assume valid user entry before validation
    userEntryValid = True
    
    #Invalid input checks
    if bankAccount.isnumeric()==False:
        print("\nERROR>> Invalid numeric input!")
        userEntryValid=False
    if len(bankAccount) >10:
        print("\nERROR>> Invalid, entry cannot be longer than 10 digits")
        userEntryValid=False

# Assuming we want user to enter "x" or "X" ro exit the script
# User entered x to exit
# "exit()" command found via Google
if bankAccount=='X' or bankAccount=='x':
    exit("Goodbye!")
    
# now pad with zeros to ensure 10 in length 
bankAccount = bankAccount.rjust(10, '0') # found on StackOverflow - https://stackoverflow.com/questions/339007/how-do-i-pad-a-string-with-zeroes
    

# After much(!) reading on Stackoverflow for this len() command and srting manipulation...
# and then finding I was over-complicating it :-(
#xs = "XXXXXXXXXX"
#displayBankAccount = xs[0:10-len(bankAccount)-4] + bankAccount[6:10]
xs = "XXXXXX"
displayBankAccount = xs + bankAccount[6:10]

# Finally output the resulting X'd account number
print(displayBankAccount)
 
 


