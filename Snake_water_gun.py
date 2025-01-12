#snake water gun

import random



x=input("Enter your choice: snake, water and gun:")
my_list=["snake","water","gun"]
random_choice=random.choice(my_list)
print("My choice:",random_choice)
if(x=="snake" and random_choice=="water"):
    print("you win")

elif(x=="snake" and random_choice=="gun"):
    print("I win")

    
elif(x=="water" and random_choice=="snake"):
    print("I win")

elif(x=="water" and random_choice=="gun"):
    print("U win")

elif(x=="gun" and random_choice=="water"):
    print("u win")

elif(x=="gun" and random_choice=="snake"):
    print("u win")

else:
    print("tie")
    
    
    

