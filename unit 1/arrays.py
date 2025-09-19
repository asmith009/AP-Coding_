# # Activity:
# # Create a function the will loop through 
# # and print each number in the list and stops at the 48.
# # In your function, the list and the Value 
# # that need to be found should be passed as arguments

# numberList = [1, 20, 39, 48, 72, 83]
# value = 48

# def NumberLoop(numberList, value):
#     for x in numberList:
#         if x == value:
#             break
#         print(x)

# NumberLoop()

# #create a function that will organize these numbers from least to greatest
# unorder = [23, 600, 4, 91, 22, 49]


mylist = [23, 600, 4, 91, 22, 49]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)