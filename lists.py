# fave_songs = [
#     "MCR - Heaven Help Us",
#     "Louis Tomlinson - Fearless",
#     "PTV - Disasterology"
# ]

# print(fave_songs[1])
# #The number in the brackets is there if you only want to list a specific placement in the list

# fave_songs = [
#     "MCR - Heaven Help Us",
#     "Louis Tomlinson - Fearless",
#     "PTV - Disasterology"
# ]

# print(fave_songs)
# fave_songs[2] = "BTS - I Need U"
# print(fave_songs)
# Replaces something in the list depending on the number position used and text entered

# fave_songs = [
#     "MCR - Heaven Help Us",
#     "Louis Tomlinson - Fearless",
#     "PTV - Disasterology"
# ]

# print(len(fave_songs))
# # States how many variables are in the list

# fave_songs = [
#     "MCR - Heaven Help Us",
#     "Louis Tomlinson - Fearless",
#     "PTV - Disasterology"
# ]

# # fave_songs.append("ADTR - Dead & Buried")
# # # .append adds something to the list at the end

# # fave_songs.pop()

# # print(fave_songs)
# # # .pop takes away the last thing added (in this example it took away the addition of ADTR i did beforehand)

# # ACTIVITY ONE

fave_websites = [
    "Twitter",
    "Twitch",
    "Youtube"
]
# # Step 1) Make a list
# fave_websites.append("Instagram")
# fave_websites.append("Reddit")
# print(fave_websites)
# # Step 2) Added 2 more websites

# fave_websites.pop()
# print(fave_websites)
# Step 3: used .pop to remove the last added site

# ACTIVITY 2
# Step 1) Research methods and use examples

food_list = [
    "Pizza",
    "Roast Dinner",
    "Chicken",
    "Pasta"
]
print(food_list)

# food_list.remove("Chicken")
# print(food_list)
# remove does as it says - removes an item you have listed from the list

# food_list.reverse()
# print(food_list)
# reverse is used to reverse the order of the list contents

# food_list.sort()
# print(food_list)
# This sort command lists all the items in the list in order- in this case alphabetical

# print(food_list.count("Pizza"))
# # the count() command lets you see how many times an item appears in a list, this command however is different than the others as it has to go inside the print bracket

# food_list.extend("Pasta")
# print(food_list)
# # The extend command spaces out every letter of the text you wanted to be extended in this case its P,a,s,t,a

food_list.extend(fave_websites)
print(food_list)
# The extend command can also be used to join lists together in this example i combinded my food list with my fave webites list to make one big list

# ACTIVITY 6/02/2020


def sandwich_order(topping, topping2, topping3, topping4, topping5):
    print("Order: sandwich with {} {} {} {} {}".format(
        topping, topping2, topping3, topping4, topping5))


sandwich_order("meatballs", "cheese", "bacon", "sausage", "and tomato sauce")
# In this example I added a new parameter, i needed to add seperate topping variables to the order and format in order for them to show

# ACTIVITY 2 6/02/2020

test_list = [
    "item 1",
    "item 2",
    "item 3"
]

test_list.insert(0, "item 4")
# This inserts something into a list the first part is where in the list it will be positioned (index position) and then next is what you want to add at the list
print(test_list)
