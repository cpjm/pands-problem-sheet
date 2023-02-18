# bank.py
# Author: Ciaran Moran
#
# Input 2 numbers (money cents), add them, 
# and print out result in human readable format.


amt1 = int(input("Enter amount 1 (in cent): "))
amt2 = int(input("Enter amount 2 (in cent): "))
amtTotal = float((amt1+amt2)/100)
print("The sum of these is: €" + format(amtTotal,',.2f')) # ref https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
