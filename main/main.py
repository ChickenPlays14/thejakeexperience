import functions.menu
import functions.writing
import functions.randomresp
import functions.weapons
import time

time.sleep(1)

functions.menu.greeting()

name = input("Name: ")

time.sleep(1)

functions.writing.Narrator1()


time.sleep(1)

functions.menu.whatwillyousay()

selection = input(name + ": ")

if selection == "1":
    functions.randomresp.jakeresponse()

else:
    functions.randomresp.jakeresponse()

time.sleep(2)

print(name + " " + "brutally murders jake with" + functions.weapons.chosenweapon)
