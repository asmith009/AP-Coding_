# Activity:
# Create a function the will loop through 
# and print each number in the list and stops at the 48.
# In your function, the list and the Value 
# that need to be found should be passed as arguments

numberList = [1, 20, 39, 48, 72, 83]
value = 48

def NumberLoop(numberList, value):
    for x in numberList:
        if x == value:
            break
        print(x)

NumberLoop()
