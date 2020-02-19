# #print(input("What is your name? > "))
# player_name = input("What is your name? >")

# print("Your name is {}. You are a {}".format(player_name, "knight"))


# print("You are currently on the 3rd floor of the bank.")
# print("This floor so far seems quiet however you still need to be alert.")
# print("You notice a security camera in the corner of the corridoor. What do you do?")

import time


def lift_option():
    time.sleep(2)
    print("You go towards the lift and enter it.")
    time.sleep(2)
    print("Once you are inside you see that the buttons for the lower floors are not illuminated.")
    print("You are unable to use the lift.")
    time.sleep(2)
    print("(Please enter B when asked to choose again. This will take you to the door option.)")
    doorlift()


def doorlift():
    choice2 = input("A or B:")
    if choice2 == "A" or choice2 == "a":
        lift_option()
    elif choice2 == "B" or choice2 == "b":
        time.sleep(2)
        print("You go towards the door and open it. There is a staircase going downwards. You go down the stairs to Floor 2.")


def third_floor():
    time.sleep(1)
    print("You are currently on Floor 3 of the bank.")
    time.sleep(2)
    print("This floor seems quiet however you still need to be alert.")
    time.sleep(2)
    print("You notice a security camera in the corner of the corridoor. What do you do?")
    time.sleep(2)
    print("A. Text Hackerman to sort it out. (This will use one of Hackerman's actions)")
    time.sleep(1)
    print("B. Ignore it.")
    time.sleep(2)
    choice = input("A or B:")
    # NEED A VARIABLE NAME FOR INPUT E.G CHOICE OR CHOICE1, CHOICE2 ETC - NEEDED FOR EVERY INPUT AND IF OPTION
    if choice == "A" or choice == "a":
        print("Hackerman recieves your text detailing the location of the camera and uses his skills to make the camera stop working.")
        time.sleep(2)
        print("You now have 2 Hackerman actions remaining")
    elif choice == "B" or choice == "b":
        print("You decide to just carry on going down the corridor even though you could be getting recorded. You hope that the camera wasn't working in the first place.")
        time.sleep(2)
    print("You have reached the end of the corridor and noticed there is a lift and a door. Which way do you go?")
    time.sleep(2)
    print("A. Go to the lift")
    time.sleep(1)
    print("B. Go to the door")
    time.sleep(2)
    doorlift()


third_floor()
