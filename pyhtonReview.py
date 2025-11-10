# create a new document called pythonReview.py and answer the following
# questions. 

# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

def schoolWork(classwork, homework):
    if classwork and homework == True:
        print('goodjob, your done.')
    elif classwork == False:
        print('you still have classwork to do.')
    elif homework == False:
        print('You still have classwork to do.')

schoolWork(True, True)

# hint: find the a operator that allows you to evaluate 2 condtions.

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

def unoReverseCard():
    userInput = input('')
    print(userInput[::-1])

unoReverseCard()

# hint: look into string reverse in w3schools

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

