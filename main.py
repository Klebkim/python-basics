from blueWhale import blueWhale
from panda import panda
from flamingo import flamingo
from chicken import chicken
import time
import random
dory = panda(False, 10, 700)
jamie = flamingo(True, 9, 250,50)
kevin = chicken(True, 2, 100, 0)

# poop_counter = 0
# while dory.check_weight() > 0:
#     dory.poop()
#     poop_counter += 1
#     print("Dory has pooped " + str(poop_counter) + " times thus far.")
#     time.sleep(0.5)

dory.check_weight()
dory.check_height()
dory.eat()
dory.extinct()
if (dory.is_it_a_boy) == True:
    print("He is a boy!")
else:
    print("He is a girl")
jamie.check_height()
jamie.check_weight()
jamie.eat()
if (jamie.is_it_a_boy) == True:
    print("He is a boy!")
else:
    print("She is a girl")
kevin.check_weight()
kevin.check_height()
kevin.eat()
kevin.lay_egg()
if kevin.is_it_a_boy == True:
    print("He is a boy")
else:
    print("She is a girl")





