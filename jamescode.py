import time

options = [1, 2, 3, 4]
inventory = ['smokebomb', 'taser', 'infrared goggles']
codename = input('What is your codename again? ')
local_items = ['hand drill', 'duffle bag', 'banana']
item_selected = 0
hackerman_uses = 3


def eventitemcheck():
    print('Your current items are: ')
    for i in inventory:
        print(i)
    time.sleep(0.2)


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

        # there needs to be a way to loop back to the start implemented here

# use this to set your events up, copy paste for each event or modify how you see fit ect


def event():
    choice = int(
        input('example event: Do you want to [1] call hackermann or [2] use a item?'))
    if choice == 1:
        print('hackermann event goes here just remove the print and put what you want')
    elif choice == 2:
        print('item select goes here')
        eventitemcheck()
        item_used = int(
            input('Which item are you going to use?([1], [2], [3], ect) '))
        if item_used == 1:
            print("You used item {} to do _____________ this and this happened  # this is where you enter what happens in your event'.format(
                inventory[0]))
            print('Item {} removed from inventory _________ something happened and the item was used up'.format(
                inventory[0]))
            inventory.pop(0)
            eventitemcheck()
        elif item_used == 2:
            print('You used item {} to do _____________ this and this happened # this is where you enter what happens in your event'.format(
                inventory[1]))
            print('Item {} removed from inventory _________ something happened and the item was used up'.format(
                inventory[1]))
            inventory.pop(1)
            eventitemcheck()
        elif item_used == 3:
            print('You used item {} to do _____________ this and this happened # this is where you enter what happens in your event'.format(
                inventory[2]))
            print('Item {} removed from inventory _________ something happened and the item was used up'.format(
                inventory[2]))
            inventory.pop(2)
            eventitemcheck()
    else:
        print('need to implement a way to restart the event that would go here')


# game start

print('Welcome to HEI$T, ' + codename + ' you can call me Hackerman')

time.sleep(1)
# replace all this stuff with yours rebecca
print('You are about to zipline down to the bank on the other side of the street. You are hooked up and ready to go but before you go you decide to grab one more item. Your current equipment consists of:')
time.sleep(3)
for i in inventory:
    time.sleep(0.2)
    print(i)

time.sleep(1)
print('You can see 3 items in your immediate area')

eventitemchoose()

event()


print('Next sequence')
