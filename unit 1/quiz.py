# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.

'A linear search is a search in which goes through one by one, or in  other words, going through in a straight line in order one by one until the end is reached.'

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.

listA = [10,24,34,35,67,98,101]

'In order to get tot he number 98, it would take 5 steps.'

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.

listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]

'Given the fact that binary search splits the list in half, it would take 4 steps to get to the number 150.'

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.

'An algorithm is technically a rule book with instructions to solve a certain kind of problem or problems. Or even to find something.'

# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.

'The O(1) time complexity would be the most efficient one beacuse i order to get to a specific floor, the elevator would need a specific number. Using this time complexity if the user presses on the exact floor they need they will be brought to the floor.'

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.

'The O(n) time complexity would be the most efficient because the way i thought about going about this is going from the latest pair of pants worn, and the most recent. In order to get here, we would go in order form leats to greatest.'

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.

class GameConsole():
    def __init__(self, name, game, storage, account):
        self.name = name
        self. game = game
        self.storage = storage
        self.account = account

    def printInfo(self):
        print('heres what game your playing')
        print('name'+ self.name)
        print('game'+ self.game)
        print('storage'+ self.storage)
        print('account'+ self.account)

    def gameChoice(fortnite, dbd, rivals):
        UserInput = input('Choose your game: fortnite, dbd, or rivals')
        if UserInput == fortnite:
            print('opening fortnite')
        elif UserInput == dbd:
            print('opening dbd')
        elif UserInput == rivals:
            print('opening rivals')
        else:
            print('you do not have this game.')

gameInfo = GameConsole(' fortnite', ' shooting game',' 18g', ' iitzMarii')

print(gameInfo)

gameInfo.printInfo()


# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 

class VideoGame():
    def __init__():