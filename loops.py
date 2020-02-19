# favourite_drinks = [
#     "Water",
#     "Hot Chocolate",
#     "Tea"
# ]

# for i in favourite_drinks:
#     print(i)
# Extracts items from list and makes the formatting look different e.g. no square brackets


# for number_index in range(10):
#     print(number_index)
# # Prints 10 times #range 10 means 0 to 9

# import random
# for random_numbers in range(6):
#     print(random.randint(1, 50))
# import random is needed to get the random numbers, the range is for how many numbers you want to be printed, and then .randint is the formatting and 1, 50 is for numbers between 1 and 50

# for counting in range(9, -1, -1):
#     print(counting)
# # making a loop to show 9 to 0, have that in the range first is where to start and second is where to end, adding another -1 makes it go through backwards

favourite_films = [
    "Iron Man 3",
    "The Polar Express",
    "Lucario and the mystery of Mew"
]

favourite_films.append("Inception")
favourite_films.append("Hidden Figures")

for i in favourite_films:
    print(i)
# In this example I added two films to the list with .append and then created a loop to extract the list without the square brackets and commas
# the i is the index and it works because the 'in' links it to the original list


def film_check():
    if favourite_films[2] == "Inception":
        print("Yes it is Inception")
    else:
        print("No this should be something else")


film_check()

# I crated a function (def) to make the film check
# This example is letting me see a specific placement within the list hence the [2] within the if, then i need to have an alternative response
