
print("You are set up to zipline accross to the bank, the rope is in place. However before you start this mission you need to choose an item.")
time.sleep(3)
print("What will you pick?")
time.sleep(1)
print("A. A handrill")
time.sleep(1)
print("B. A dufflebag")
time.sleep(1)
 print("C. A banana")
  firstchoice = input("A, B or C:")
   if firstchoice == "A" or firstchoice == "a":
        handrill()
        time.sleep(2)
    elif firstchoice == "B" or "b":
        dufflebag()
    elif firstchoice == "C" or firstchoice == "c":
        banana()
        time.sleep(2)

        # intro option


def handrill():
    print("[Insert what happens if you pick this here]")
    time.sleep(2)
    third_floor()

# intro option


def dufflebag():
    print("[Insert what happens if you pick this here]")
    time.sleep(2)
    third_floor()

# intro option


def banana():
    print("[Insert what happens if you pick this here]")
    time.sleep(2)
    third_floor()
