import random
import time


def Narrator1():
    print("You have met Jake!")


def jakeresponse():
    response = random.randint(0, 10)
    stock = "Jake:"
    spc = " "

    if response == 1:
        print(stock + spc + "Bet")

    elif response == 2:
        print(stock + spc + "Bruh")

    elif response == 3:
        print(stock + spc + "W H A T")

    elif response == 4:
        print(stock + spc + "*plays soundboard*")

    elif response == 5:
        print(stock + spc + "*breathes in* MALD")

    elif response == 6:
        print(stock + spc + "*starts talking about some random history shite")

    elif response == 7:
        print(stock + spc + "Sadge")

    elif response == 8:
        print(stock + spc + "noooo")

    elif response == 9:
        print(stock + spc + "*starts explaining something highly explicit in excruciating detail*")

    elif response == 10:
        print(stock + spc + "He's not german, he's AUSTRIAN")


def greeting():
    global name
    print("Greetings user! What is your name?")


def whatwillyousay():
    print(" ")
    print("What will you say?")
    print("1) Hi")
    print("2) Send meme")
    print("3) Say nothing")


def weapons():
    global chosenweapon
    weapon = random.randint(0, 10)

    if weapon == 1:
        chosenweapon = " an axe to the face"

    elif weapon == 2:
        chosenweapon = " a nuclear warhead"

    elif weapon == 3:
        chosenweapon = " a stick of uranium 235 up the ass"

    elif weapon == 4:
        chosenweapon = " an M4A1 assault rifle"

    elif weapon == 5:
        chosenweapon = " 28 stab wounds"

    elif weapon == 6:
        chosenweapon = " a bowling ball"

    elif weapon == 7:
        chosenweapon = " lots and lots of acid"

    elif weapon == 8:
        chosenweapon = " Chloe (she sent him to the shadow realm)"

    elif weapon == 9:
        chosenweapon = " a pipe bomb"

    elif weapon == 10:
        chosenweapon = " 9/11"



time.sleep(1)

greeting()

name = input("Name: ")

time.sleep(1)

Narrator1()

time.sleep(1)

whatwillyousay()

selection = input(name + ": ")

if selection == "1":
    jakeresponse()

else:
    jakeresponse()

time.sleep(2)

weapons()

print(name + " " + "brutally murders jake with" + chosenweapon)