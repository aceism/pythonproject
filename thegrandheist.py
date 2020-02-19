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
# REBECCA'S FLOOR
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
# game start
# JAMES' CODE
print('Welcome to HEI$T, ' + codename + ' you can call me Hackerman')
time.sleep(1)
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
        time.sleep(0.2)
        print(i)
def eventitemchoose():
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
# JACKS CODE
security_access = 0
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
    print("You now have access to the security system thanks to hackerman.")
    floor_2_good_leave()
def security_bad():
    print("You now have security access but people may notice the unconscious guard and rase the alarm.")
    time.sleep(1)
    security_good()
def security_good():
    print("You now have access to the security system.")
    time.sleep(2)
    floor_2_good_leave()
def security_bad_input():
    print("Please choose A, B or C.")
    print("The security station is a small room with a desk, behind the desk a guard watches over a series of monitors. You can either A. Knockout the guard, B. Distract the guard with ITEM or C. Call Hackerman to hack the security system for you.")
    time.sleep(2)
    security_station_options = input("Choose A, B or C. ")
    if security_station_options == "A" or security_station_options == "a":
        print(
            "You attack and knock out the guard, you can now access the security station.")
        time.sleep(1)
        security_bad()
    elif security_station_options == "B" or security_station_options == "b":
        print("You distract the guard with ITEM, causing them to leave the security station, you can now access the security station.")
        time.sleep(1)
        security_good()
    elif security_station_options == "C" or security_station_options == "c":
        print("You call up hackerman and get him to hack the security system for you.")
        time.sleep(1)
        security_hackerman()
    else:
        security_bad_input()
def security_station_fn():
    print("The security station is a small room with a desk, behind the desk a guard watches over a series of monitors. You can either A. Knockout the guard, B. Distract the guard with ITEM or C. Call Hackerman to hack the security system for you.")
    time.sleep(2)
    security_station_options = input("Choose A, B or C. ")
    if security_station_options == "A" or security_station_options == "a":
        print(
            "You attack and knock out the guard, you can now access the security station.")
        time.sleep(1)
        security_bad()
    elif security_station_options == "B" or security_station_options == "b":
        print("You distract the guard with ITEM, causing them to leave the security station, you can now access the security station.")
        time.sleep(1)
        security_good()
    elif security_station_options == "C" or security_station_options == "c":
        print("You call up hackerman and get him to hack the security system for you.")
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
    main_room_fn()
def main_room_bad_input():
    print("Please choose either A or B.")
    time.sleep(1)
    print("Do you A. Attack the guards or B. Investigate the area")
    time.sleep(1)
    floor_2_choice_2 = input("A or B ")
    if floor_2_choice_2 == "A" or floor_2_choice_2 == "a":
        print("You begin causing a comotion and draw the attention of the guards, when they approach you attack but you are quickly arrested, your mission ends here.")
        time.sleep(1)
        floor_2_bad_leave()
    elif floor_2_choice_2 == "B" or floor_2_choice_2 == "b":
        print("You begin investigating the main room, making sure not to draw attention to yourself, you learn the pattern the guards take and the main exits from this floor, a set of stairs and an elevator both which lead to the first floor.")
        time.sleep(1)
        print("While searching this floor you find pickup and decide to take it.")
        time.sleep(1)
        print("PICKED UP Pickup!")
        floor_2_good_leave()
    else:
        main_room_bad_input()
def main_room_fn():
    print("The main room is a large open space with people coming too and throw on their buisness, guards patrol the area, keeping an eye out for potential criminal activity. You can either attack the guards and try to get through the bank as quickly as possible or investigate this floor ofthe bank and find a way around security.")
    time.sleep(2)
    print("Do you A. Attack the guards or B. Investigate the area")
    time.sleep(1)
    floor_2_choice_2 = input("A or B ")
    if floor_2_choice_2 == "A" or floor_2_choice_2 == "a":
        print("You begin causing a comotion and draw the attention of the guards, when they approach you attack, swinging wildly at the guards and running to the nearest exit.")
        time.sleep(1)
        floor_2_bad_leave()
    elif floor_2_choice_2 == "B" or floor_2_choice_2 == "b":
        print("You begin investigating the main room, making sure not to draw attention to yourself, you learn the pattern the guards take and the main exits from this floor, a set of stairs and an elevator both which lead to the first floor.")
        time.sleep(1)
        print("While searching this floor you find pickup and decide to take it.")
        time.sleep(1)
        print("PICKED UP Pickup!")
        floor_2_good_leave()
    else:
        main_room_bad_input()
def door_incorrect_input():
    print("Please choose either A or B.")
    time.sleep(1)
    floor_2_choice_1 = input(
        " A. The main room of the bank or B. Security Station? ")
    if floor_2_choice_1 == "A" or floor_2_choice_1 == "a":
        main_room_fn()
    elif floor_2_choice_1 == "B" or floor_2_choice_1 == "b":
        security_station_fn()
    else:
        door_incorrect_input()
def floor_2_enter():
    floor_3_exit = "the stairs"
    print("You enter the 2nd floor from {}".format(floor_3_exit))
    time.sleep(2)
    print("You see a door leading to A. The main room of the bank and B. The Security Station.")
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
floor_2_enter()
# This is to run the second floor
print('------Next sequence------')
# Start_of_level
yes_no = ["yes", "no",]
directions = ["left", "right",]
response = ''
def third_choice():
    response_three = input('You come to the door, the flashing green keypad catches your attention. A question appears: "What always ends everything?" Please type in your answer.')
    time.sleep(1)
    if response_three == "g":
        print ("You hear a click, the keypad flashes eratically and the door swings open, the answer was correct and you have now been granted access to the final floor, the vault is close.")
        time.sleep(1)
        print("---------------------------------------------")
        time.sleep(1)
        print('Next function choice here - next section of the game goes here.')
    else:
        print ("The answer is incorrect.")
        time.sleep(1)
        print ("Please try again.")
        time.sleep(1)
        print("---------------------------------------------")
        third_choice()
def second_choice():
    attack_guards = "1"
    hackerman_distraction = "2"
    print ("With great haste, you take cover behind some of the clutter. Taking a quick peek they appear to be quite formidable if approached head on, armed with walky talkies to call for back-up and batons. Your gut tells you a distraction could be what is needed to deal with them.")
    time.sleep(1)
    print("(1) Do you attack the guards?")
    time.sleep(1)
    print("(2) Do you call upon Hackerman to cause a distraction?")
    #Possibly include the code for Hackerman number of uses
    #If this is included maybe include a code to use an item on the player to use as a distraction?
    #print("(3) Do you throw a tool across the room to cause a distraction?")
    time.sleep(1)
    response_two = input("1 or 2?") #if we add the code to use an item, add "or 3?" in the brackets.
    if response_two == "1":
        time.sleep(1)
        print("Going against your gut instinct, you decide to pick a fight with the 2 guards, they appear dimwitted however they prove to be compitent in a scrap and with there being 2 of them they easily overpower you and subdue you.")
        time.sleep(1)
        print("You have been captured.")
        time.sleep(1)
        print("Game over.")
        time.sleep(1)
        print("You will now be asked to choose again.")
        time.sleep(1)
        print("---------------------------------------------")
        second_choice()
    elif response_two == "2":
        print("Your faithful companion Hackerman received your cry for help and through sheer technical skill he was successfully able hack into the walky talkies and drain the batteries.")
        time.sleep(1)
        print("The guards being notified by the beepeing of their walky talkies are aware that the batteries are low. They proceed to leave the room in search of fresh batteries.")
        time.sleep(1)
        print("The coast is clear, there is only the final door blocking your way to the final floor.")
        time.sleep(1)
        third_choice()
    #else response_two == "3":
        #print("Which tool do you wish to use?")
        #then include the code for the inventory list
        #third_choice()
def first_choice():
    print("After successfully evading the guards and security systems on Floor 2, you make your way down to the 1st floor.")
    time.sleep(1)
    print("The layout of this floor appears to be very simple, as there is only one way to go. Forward.")
    time.sleep(1)
    print("You begin to move down the corridor gingerly, being cautious to not create too much noise, you encounter a split in your path, a corridor to the left and one to the right.")
    time.sleep(1)
    print("(1) Do you go left")
    time.sleep(1)
    print("(2) Do you go right?")
    response = input("1 or 2?")
    time.sleep(1)
    
    if response == "1": 
        print("You creep with the agility of a cat down the corridor. An intimidating steel door blocks your path, conviniently this door is unlocked. You muster the courage to enter.")
        time.sleep(1)
        print ("You enter into a huge room, filled with clutter and trash, two gormless guards block the only other door in the room.")
        time.sleep(1)
        second_choice()
    elif response == "2":
        print("You follow the other corridor and encounter a small wooden door with a rusty old door knob, a quick wiggle and shake of the handle, the door remains shut.")
        time.sleep(1)
        print("Do you:")
        time.sleep(1)
        print("(1) Do you want to kick the door open?")
        time.sleep(1)
        print("(2) Do you decide not to risk it and go back?")
        time.sleep(1)
        response = input("1 or 2?")
        if response == "1":
            print("You use all your strength to force the door open, after a quick struggle the door swings open, the alarm rings, alerting the entire building to your prescence")
            time.sleep(1)
            print("Your recklessness has jeprodised your adventure.")
            time.sleep(1)
            print("Game over.")
            time.sleep(1)
            print("---------------------------------------------")
            time.sleep(1)
            first_choice()
        elif response == "2":
            print ("You decide to not risk it, as you suspect it could perhaps be a trap. You move back and decide whether to go left or right again.")
            time.sleep(1)
            first_choice()
        time.sleep(1)
        print("---------------------------------------------")
        time.sleep(1)
        first_choice()
    else:
        
        print("I didn't understand that.")
        time.sleep(1)
        print('Please type in either "1" or "2"')
        time.sleep(1)
        print("---------------------------------------------")
        first_choice()
first_choice()