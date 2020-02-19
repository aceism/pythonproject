# def press_grind_beans():
#     print("Grinding for 20 seconds")


# # def is for functions and () are needed afterwards
# press_grind_beans()
# # this being here makes the function work

# coffee_is_grinding = True


# def press_grind_beans():
#     if coffee_is_grinding:
#         print("The coffee is grinding")
#     else:
#         print("The coffee is not grinding")
# # Using if statments to have different options considering the variable true or false


# press_grind_beans()


# # def coffee_order(size, types):
# #     print("The size of the drink is {} and the type is {}".format(size, types))
# # # Used the braces brackets and format to make the terminal readout easier
# # # words in the brackets after cash_withdrawl are like variables


# # coffee_order("small", "coffee")
# # coffee_order("large", "tea")
# # coffee_order("medium", "water")
# # # this shows the 3 different transactions, words in brackets are parameters and are linked to the words in the brackets for the first line and the formatting brackets


# # def add_up(num1, num2):
# #     return num1 + num2
# # # Does the calculation but remembers it and doesnt print it


# # add_up(7, 3)
# # print(add_up(2, 5))

# # # This is to add numbers up - it only shows the printed variable


# # def multiply_by_nine_fifths(celsius):
# #     return celsius * (9/5)


# # def get_fahrenheit(celsius):
# #     return multiply_by_nine_fifths(celsius) + 32


# # print("The temperature is {}".format(get_fahrenheit(15)))
# # # Converts celsius to fahrenheit


# # # ACTIVITY 1


# # def take_order(topping, size):
# #     print("Pizza with {} and is {}".format(topping, size))


# # take_order("pineapple", "small")
# # In this example I added a new parameter

# # ACTIVITY 2


# bank_total = 100

# pin = 230


# def cash_amount(withdraw):
#     print("You want to withdraw {} and you have {} in your account".format(
#         withdraw, bank_total))
#     if pin == 123:
#         print("Pin accepted")
#     else:
#         print("Pin rejected")

#     if bank_total >= 200:
#         print("You have enough funds")
#     elif bank_total <= 200:
#         print("You do not have enough funds")


# cash_amount(300)
# cash_amount(400)


# PART 2 Trying to get the if statements in one sentance

bank_total = 100

pin = 123


def cash_amount(withdraw):
    print("You want to withdraw {} and you have {} in your account".format(
        withdraw, bank_total))
    if pin == 123 and bank_total >= withdraw:
        print("Pin accepted", ". You have enough funds")
    elif pin != 123 and bank_total <= withdraw:
        print("Pin rejected", ", but you do not have enough funds")
    if pin == 123 and bank_total <= withdraw:
        print("Pin accepted", ". You do not enough funds")
    elif pin != 123 and bank_total >= withdraw:
        print("Pin rejected", ", but you have enough funds")


cash_amount(101)


# def multiply(num1, num2):
#     return num1 * num2
# # Does the calculation but remembers it and doesnt print it


# multiply(7, 3)
# print(multiply(2, 5))
