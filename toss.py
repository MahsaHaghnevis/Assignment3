#
##
### created by Yseeva
## july 30
#


import random
import time
def GenRand():
    return random.randint(1,6)
print("------- WELCOME TO DICE GAME --------")
print("rules are simple:\n * if u got 6 you can roll 2 times \n * anf if not you only have an another try")
input("---->Enter to start :")

roll=GenRand()
tries=1
print(" you had " ,'\t' , roll , '\t' , f"So you have {tries} left")

while tries!=0:
    roll=GenRand()
    #print(" you had " ,'\t' , roll , '\t' , f"So you have {tries} left")
    if roll == 6 :
         tries+=2
    else :
        tries-=1
    
    print(" you had " ,'\t' , roll , '\t' , f"So you have {tries} left")

print(" -------- Done --------")
    
        
        