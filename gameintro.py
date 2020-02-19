# This is for the intro to the bank heist game - just the text and not the item options
# These can be added in later

import time

#print(input("What is your name? > "))
player_name = ("Agent ") + input("What is your agent name? >")

print("Your name is {}.".format(player_name))
time.sleep(3)


def game_intro():
    print("The day has finally arrived.")
    time.sleep(3)
    print("All of the months of preparation has lead up to this moment.")
    time.sleep(3)
    print("You secretly were feeling nervous about undertaking this mission. At least you had Hackerman outside in the van to help out if needed.")
    time.sleep(3)
    print("Currently you are stationed on the building opposite the targeted bank.")
    time.sleep(3)
    print("You are set up to zipline accross to the bank, the rope is in place. However before you start this mission you need to choose an item.")
    time.sleep(3)
    print("What will you pick?")
    print("A. A handrill")
    print("B. A dufflebag")
    print("C. A banana")
    firstchoice = input("A, B or C:")
    if firstchoice == "A" or firstchoice == "a":
        print("[Insert what happens if you pick handrill here].")
        time.sleep(2)
    if firstchoice == "B" or "b":
        print("[Insert what happens if you pick a dufflebag here]")
    elif firstchoice == "C" or firstchoice == "c":
        print("[Insert what happens if you pick the banana here].")
        time.sleep(2)
# We need a choice of item here


game_intro()
