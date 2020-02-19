# # music = "No music"
# # # If I change this it changes the outcome of the if

# # if music == "Rebecca's music":
# #     print("Oh no it's MCR again")
# # #    This is one result
# # elif music == "No music":
# #     print("Peace and quiet")
# # # This is another outcome
# # else:
# #     print("What music is playing?")

# # ACTIVITY
# # Create a variable called age. Write and if statement that logs answers

# age = 17
# country = "USA"
# # The variable

# if age >= 18 and country == "UK":
#     print("Yes I can serve you")
# # >= is equal to or greater than
# elif age <= 17 and country == "UK":
#     print("You are not old enough")
# # <= equal to or less than
# else:
#     print("How old are you?")

# # ACTIVTY 2

# place = "Manchester"
# weather = "Cloudy"
# # These are the variables

# if place == "Manchester" and weather == "Sunny":
#     print("Check agin")
# #
# elif place == "Manchester" and weather == "Cloudy":
#     print("Obviously")
# else:
#     print("What is isnt raining?")

# # ACTIVITY 3

# day = "Monday"
# # This is the variable

# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("When's the weekend")

# # CHALLENGE 1
# # Create a variable called password and check amount of letters

# print(len("password"))
# password = '12345678'

# if len(password) >= 8:
#     print("Password can be used")
# elif len(password) < 8:
#     print("Password is too short")

# len is used for length and is outside of the brackets for the word password so it works with it

# # CHALLENGE 2
# # Create a variable called num

# num = 19
# # This is a variable

# if num % 3 == 0 or num % 5 == 0:
#     print("This number is divisible by 3 or 5")
# else:
#     print("This number is not divisible by 3 or 5")
# % is used for divison with no remainer
# == means equal and its == 0 as it doesnt leave a remainer when divided

# CHALLENGE 3

num = 9
# This is the variable

if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print("It isnt divisible by 3 or 5")

# For this challenge I had to have the option for both numbers to be first in order for fizzbuzz to show in the terminal

# CHALLENGE 4
# Find out if a number is a palindrome

num = 2002
forward_string = str(num)
backward_string = forward_string[::-1]
if int(forward_string) == int(backward_string):
    print("This is a palindrome")
else:
    print("This is not a palindrome")


# ACTIVITY

space1 = "x"
space2 = "x"
space3 = "x"
space4 = " "
space5 = "x"
space6 = " "
space7 = "o"
space8 = " "
space9 = " "
print("     |    |     ")
print("  {}  | {}  |   {}  ".format(space1, space2, space3))
print("     |    |     ")
print("----------------")
print("     |    |     ")
print("   {} |  {} |  {}   ".format(space4, space5, space6))
print("     |    |     ")
print("----------------")
print("     |    |     ")
print("   {} |  {} |   {} ".format(space7, space8, space9))
print("     |    |     ")


if space1 == "x" and space2 == "x" and space3 == "x":
    print("Winner")
else:
    print("Not winning")

if space1 == "o" and space2 == "o" and space3 == "o":
    print("Winner")
else:
    print("Not winning")


# ACTIVTY 2
# Had to make a statment that checks ticket prices
age = 70

if age <= 17:
    print("Price is £8")
elif age >= 59:
    print("Price is £7.50")
elif age >= 18:
    print("Price is £10.95")
