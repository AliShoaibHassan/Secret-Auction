# import random
#
# words = [
#     'ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam',
#     'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle',
#     'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama',
#     'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda',
#     'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino',
#     'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider',
#     'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel',
#     'whale', 'wolf', 'wombat', 'zebra'
# ]
#
# figure = [
#     r'''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
#   ========''', r'''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
#   ========''', r'''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
#   ========''', r'''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
#   ========''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
#   ========''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
#   ========''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
#   ========'''
# ]
#
#
# word = random.choice(words)
# length = len(word)
# print(word)
# quest = list(word)
# print(quest)
#
# guess =[]
# for i in range(0, length):
#     print("_", end="")
#     guess.append("_")
#
# letter_count = 0
# count = 0
#
# while guess != quest and count < 7:
#     letter = input("\nEnter your guess for the letter: \n")
#
#     # Check if the letter is in the word
#     if letter in word:
#         # Update the guessed letters
#         for i, let in enumerate(word):
#             if let == letter:
#                 guess[i] = letter
#     else:
#
#         print(figure[count])
#         count += 1
#
#
#     print("Current guess: " + "".join(guess))
#
# if count == 7:
#     print("GAME OVER! YOU LOST!")
#
# else:
#     print("CONGRATULATIONS! YOU WON THE GAME!")




# DAY 8!!!!!!!


# def greet(name, location):
#     print(f"Hello {name}. You live in {location}.")
#
# #Even if we change the order of our arguments, The result will be correct as we have used our parameters to assign them values while calling the function
# greet(location="Isb", name="Ali")
#
# word = list("Ali")


# LOVE CALCULATOR APP
# def calculate_love_score(name1, name2):
#     # Convert both names to lowercase
#     name1 = name1.lower()
#     name2 = name2.lower()
#
#     # Convert names to lists
#     word1 = list(name1)
#     word2 = list(name2)
#
#     count_true = 0
#     count_love = 0
#
#     # Count occurrences of 't', 'r', 'u', 'e' in the first name
#     for char in word1:
#         if char in ["t", "r", "u", "e"]:
#             count_true += 1
#
#     # Count occurrences of 't', 'r', 'u', 'e' in the second name
#     for char in word2:
#         if char in ["t", "r", "u", "e"]:
#             count_true += 1
#
#
#     for char in word1:
#         if char in ["l", "o", "v", "e"]:
#             count_love += 1
#
#
#     for char in word2:
#         if char in ["l", "o", "v", "e"]:
#             count_love += 1
#
#     # Output the count
#     print(f"{count_true}{count_love}")
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")



# DAY 9!!!!!!

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
#
# for key in student_scores:
#
#     if 91 <= student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
#
#     elif 81 <= student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectations"
#
#     elif 71 <= student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#
#     else:
#         student_grades[key] = "Fail"
#
# print(student_grades)
#
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
# }
#
# print(travel_log["France"][1])


# SECRET AUCTION PROJECT

def welcome():
    print("WELCOME TO THE SECRET AUCTION PROGRAM!")

    logo = r'''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''

    print(logo)

bids = {}
ppl = "yes"

while ppl == "yes":
    welcome()
    name = input("Enter your name: ")
    bid = float(input("Enter your bid: $"))
    bids[name] = bid

    ppl = input("Are there any more bidders? Yes/No: ").lower()
    print("\n" *30)

highest = 0
name = ""
for key in bids:
    if bids[key] > highest:
        highest = bids[key]
        name = key


print(f"\n\nThe auction was won by {name}, with the bid of ${highest}")

