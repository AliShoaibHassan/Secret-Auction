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

