FILENAME = "count.txt"
def readNumber():
 with open(FILENAME) as f:
    number = int(f.read())
    return number
# test it
num = readNumber()
print ("Initial file contents: ", num)

def writeNumber(number):
 with open(FILENAME, "wt") as f:
    # write takes a string so we need to convert
    f.write(str(number))
# test it
writeNumber(3)

# test it
num = readNumber()
print ("after writing 3 :", num)
