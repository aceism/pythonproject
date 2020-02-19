#print(input("What is your name? > "))
import time
options = [1, 2, 3, 4]
inventory = ['Smokebomb', 'Taser', 'Infrared goggles']
codename = input('What is your codename again? ')
local_items = ['Hand drill', 'Duffle bag', 'Banana']
item_selected = 0
hackerman_uses = 3

# This it for when the code checks the items you currently have


def eventitemcheck():
    time.sleep(1)
    print('Your current items are: ')
    for i in inventory:
        print(i)
    time.sleep(2)

# third floor option


def lift_option():
    time.sleep(2)
    print("You go towards the lift and enter it.")
    time.sleep(2)
    print("Once you are inside you see that the buttons for the lower floors are not illuminated.")
    print("You are unable to use the lift.")
    time.sleep(2)
    print("(Please enter B when asked to choose again. This will take you to the door option.)")
    doorlift()

# third floor option


def doorlift():
    choice2 = input("A or B:")
    if choice2 == "A" or choice2 == "a":
        lift_option()
    elif choice2 == "B" or choice2 == "b":
        time.sleep(2)
        print("You go towards the door and open it. There is a staircase going downwards. You go down the stairs to Floor 2.")

# FLOOR 3 - REBECCA'S CODE


def third_floor():
    time.sleep(2)
    print("After successfully entering the building you are currently on Floor 3 of the bank.")
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
    time.sleep(1)
    print("You have reached the end of the corridor and noticed there is a lift and a door. Which way do you go?")
    time.sleep(2)
    print("A. Go to the lift")
    time.sleep(1)
    print("B. Go to the door")
    time.sleep(2)
    doorlift()


# game start
# JAMES' CODE


print('Welcome to HEI$T, ' + codename + ' you can call me Hackerman')

time.sleep(1)

# REBECCA + JAMES' CODE


def game_intro():
    print("The day has finally arrived.")
    time.sleep(2)
    print("All of the months of preparation has lead up to this moment.")
    time.sleep(2)
    print("You secretly were feeling nervous about undertaking this mission. At least you had Hackerman outside in the van to help out if needed.")
    time.sleep(2)
    print("Currently you are stationed on the building opposite the targeted bank.")
    time.sleep(2)
    print('You are about to zipline down to the bank on the other side of the street. You are hooked up and ready to go but before you go you decide to grab one more item. Your current equipment consists of:')
    time.sleep(2)
    for i in inventory:
        time.sleep(1)
        print(i)


def eventitemchoose():
    time.sleep(1)
    print(local_items)
    item_selected = int(
        input('Which item are you going to take with you (1, 2, 3): '))
    if item_selected == 1:
        print('You quickly grabbed the {}'.format(local_items[0]))
        inventory.append('{}'.format(local_items[0]))
        eventitemcheck()
    elif item_selected == 2:
        print('You quickly grabbed the {}'.format(local_items[1]))
        inventory.append('{}'.format(local_items[1]))
        eventitemcheck()
    elif item_selected == 3:
        print('You quickly grabbed the {}'.format(local_items[2]))
        inventory.append('{}'.format(local_items[2]))
        eventitemcheck()
    else:
        print('Invalid option try again')

# FLOOR 2 - JACKS CODE


def exit_via_lift_good():
    print("You descend to floor 1 via the lift.")
    # FLOOR 1 GO HERE


def exit_via_stairs_good():
    print("You descend to floor 1 via the stairs.")
    # FLOOR 1 GO HERE


def floor_2_good_incorrect():
    print("Please choose A or B.")
    floor_2_good_choice = input(
        "Do you: A. use the lift to go to floor 1. B. take the stairs to floor 1.")
    if floor_2_good_choice == "A" or floor_2_good_choice == "a":
        time.sleep(1)
        exit_via_lift_good()
    elif floor_2_good_choice == "B" or floor_2_good_choice == "b":
        time.sleep(1)
        exit_via_stairs_good()
    else:
        floor_2_good_incorrect()


def floor_2_good_leave():
    print("You can now head to Floor 1.")
    floor_2_good_choice = input(
        "Do you: A. use the lift to go to floor 1. B. take the stairs to floor 1.")
    if floor_2_good_choice == "A" or floor_2_good_choice == "a":
        time.sleep(1)
        exit_via_lift_good()
    elif floor_2_good_choice == "B" or floor_2_good_choice == "b":
        time.sleep(1)
        exit_via_stairs_good()
    else:
        floor_2_good_incorrect()


def security_hackerman():
    print("hackerman does the thing, you can now get security access.")
    hackerman_uses -= 1
    security_good()


def security_bad():
    print("You do the bad thing, you can now get security access but someone may notice bad thing.")
    time.sleep(1)
    security_good()


def security_good():
    print("Get Security Access")
    time.sleep(2)
    floor_2_good_leave()


def security_bad_input():
    print("Please choose A, B or C.")
    security_option = input("Security station options A, B, C here")
    if security_option == "A" or security_option == "a":
        print("do Action A")
        time.sleep(1)
        security_bad()
    elif security_option == "B" or security_option == "b":
        print("do Action B")
        time.sleep(1)
        security_good()
    elif security_option == "C" or security_option == "c":
        print("do Action C")
        time.sleep(1)
        security_hackerman()
    else:
        security_bad_input()


def security_station_fn():
    print("Security station description here")
    time.sleep(2)
    print("Security station options A, B, C here")
    if A:
        print("do Action A")
        time.sleep(1)
        security_bad()
    elif B:
        print("do Action B")
        time.sleep(1)
        security_good()
    elif C:
        print("do Action C")
        time.sleep(1)
        security_hackerman()
    else:
        security_bad_input()


def exit_via_lift_bad():
    print("You descend to floor 1 via the lift.")

    # FLOOR 1 GO HERE


def exit_via_stairs_bad():
    print("You descend to floor 1 via the stairs.")

    # FLOOR 1 GO HERE


def bad_leave_input():
    print("Please Choose A or B.")
    time.sleep(1)
    print("You need to leave this floor quickly, do you take A. The stairs or B. The lift.")
    time.sleep(1)
    floor_2_bad_exit = input("A or B? ")
    if floor_2_bad_exit == "A" or floor_2_bad_exit == "a":
        exit_via_stairs_bad()
    elif floor_2_bad_exit == "B" or floor_2_bad_exit == "b":
        exit_via_lift_bad()
    else:
        bad_leave_input()


def floor_2_bad_leave():
    print("Security is now on HIGH ALERT for you.")
    time.sleep(2)
    print("You need to leave this floor quickly, do you take A. The stairs or B. The lift.")
    time.sleep(1)
    floor_2_bad_exit = input("A or B? ")
    if floor_2_bad_exit == "A" or floor_2_bad_exit == "a":
        exit_via_stairs_bad()
    elif floor_2_bad_exit == "B" or floor_2_bad_exit == "b":
        exit_via_lift_bad()
    else:
        bad_leave_input()


def main_room_bad_input():
    print("Please choose either A or B.")
    time.sleep(1)
    floor_2_choice_2 = input("Do Thing A or Thing B?")
    if floor_2_choice_2 == "A" or floor_2_choice_2 == "a":
        print("You do Thing A.")
        time.sleep(1)
        floor_2_bad()
    elif floor_2_choice_2 == "B" or floor_2_choice_2 == "b":
        print("You do Thing B.")
        time.sleep(1)
        print("You find Pickup 1")
        time.sleep(1)
        print("PICKED UP Pickup 1!")
        floor_2_good()
    else:
        main_room_bad_input()


def main_room_fn():
    print("Main Room Details Here")
    time.sleep(2)
    print("Main Room Choices Here")
    time.sleep(1)
    floor_2_choice_2 = input("Do Thing A or Thing B?")
    if floor_2_choice_2 == "A" or floor_2_choice_2 == "a":
        print("You do Thing A.")
        time.sleep(1)
        floor_2_bad_leave()
    elif floor_2_choice_2 == "B" or floor_2_choice_2 == "b":
        print("You do Thing B.")
        time.sleep(1)
        print("You find Pickup 1")
        time.sleep(1)
        print("PICKED UP Pickup 1!")
        floor_2_good_leave()
    else:
        main_room_bad_input()


def door_incorrect_input():
    print("Please choose either A or B.")
    time.sleep(1)
    floor_2_choice_1 = input(" A. MAINROOMNAMEHERE or B. Security Station? ")
    if floor_2_choice_1 == "A" or floor_2_choice_1 == "a":
        main_room_fn()
    elif floor_2_choice_1 == "B" or floor_2_choice_1 == "b":
        security_station_fn()
    else:
        door_incorrect_input()


def floor_2_enter():
    floor_3_exit = "the stairs"
    time.sleep(2)
    print("You enter the 2nd floor from {}".format(floor_3_exit))
    time.sleep(2)
    print("You see a door leading to A. MAINROOMNAMEHERE and B. The Security Station.")
    time.sleep(1)
    print("Which door do you go through?")
    time.sleep(1)
    floor_2_choice_1 = input(" A. or B. ")
    if floor_2_choice_1 == "A" or floor_2_choice_1 == "a":
        main_room_fn()
    elif floor_2_choice_1 == "B" or floor_2_choice_1 == "b":
        security_station_fn()
    else:
        door_incorrect_input()


# runs game
game_intro()

eventitemchoose()

# Use this to get the floors to be linked
print('------Next sequence------')
third_floor()
# This is to run the third floor
print('------Next sequence------')
time.sleep(1)
floor_2_enter()
