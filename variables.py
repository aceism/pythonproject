# name = "Rebecca"
# # name is a variable
# print(name)
# # need to print the variable

# age = "22"

# print(age)
# # to print different options under the same variable
# # you need to re-do it

# age = "50"

# print(age)

# age = "21"
# print(age)

# # favourite_officer = "bobby"
# # print("My favourite officer is " + favourite_officer + ", because he is the best")

# # favourite_drink = "water"
# # print("My favourite drink is {} and my age is {}".format(favourite_drink, age))
# # # same formula as before but uses different brackets - good for multiple variables

# # i = 10
# # i += 2
# # print(i)
# # # in this i did addition so 10 + 2 is 12

# # i = 12
# # i *= 2
# # print(i)
# # # in this I did 12 multiplied by 2

# # i = 24
# # i /= 2
# # print(i)
# # # in this example I did 24 divided by 2

# # i = 20
# # i -= 6
# # print(i)
# # # in this example I did 20 minus 6

# ACTIVITY 1

import datetime
name = "Rebecca"
age = "21"
favourite_colour = "blue"

print("My name is {} and my age is {} and my favourite colour is {}".format(
    name, age, favourite_colour))

# Here i have printed out my name, age and favourite colour and used the structure with the other brackets as it is easier to input the variables that way

# ACTIVITY 2

breakfast1 = "cereal"
breakfast2 = "toast"


print("For breakfast I could have {} or {}".format(breakfast1, breakfast2))

breakfast3 = "bacon"
breakfast = "pizza"

print("For breakfast tomorrow I could have {} or {}".format(breakfast3, breakfast))

lunch1 = "sandwich"
lunch2 = "jacket potato"


print("For lunch I could have {} or {}".format(lunch1, lunch2))

tea1 = "pasta"


tea2 = "chicken"


print("For tea I could have {} or {}".format(tea1, tea2))

# During this I learnt I dont need to print out the variables e.g tea1
# I also used the braces bracket forumla as I find it easier to add the forumlas

# ACTIVITY 3
todays_date = datetime.date.today()
my_birthday = datetime.date(2020, 3, 21)
days_to_birthday = my_birthday - todays_date
print(days_to_birthday)

# ACTIVITY 4

space1 = "x"
space2 = "o"
space3 = " "
space4 = "x"
space5 = "x"
space6 = " "
space7 = "o"
space8 = " "
space9 = " "
print("     |    |     ")
print("  {}  | {} |   {}  ".format(space1, space2, space3))
print("     |    |     ")
print("----------------")
print("     |    |     ")
print("   {} |  {} |  {}   ".format(space4, space5, space6))
print("     |    |     ")
print("----------------")
print("     |    |     ")
print("   {} |  {} |   {} ".format(space7, space8, space9))
print("     |    |     ")
