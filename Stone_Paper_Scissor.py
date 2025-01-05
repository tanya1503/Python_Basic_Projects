
import random
i=0
u=0
t=int(input("Enter number of time u want to play"))

if(t<=0):
    print("enter a natural number")
    t=int(input("Enter number of time u want to play"))

    
if (t%2==0):
    print("please write a odd number")
    t=int(input("Enter number of time u want to play"))

     
for x in range(t):
        x=input("Enter your take: stone, paper or siccisor?")
        my_list = ['stone', 'paper', 'scissor']
        random_choice = random.choice(my_list)
        print("My choice:",random_choice)
        if(x=="paper" and random_choice=="scissor"):
            print("I win")
            i+=1
        elif (x=="scissor" and random_choice=="paper"):
                print("you win")
                u+=1
        elif (x=="stone" and random_choice=="paper"):
            print("I win")
            i+=1
            
        elif (x=="paper" and random_choice=="stone"):
            print("you win")
            u+=1
        elif (x=="scissor" and random_choice=="stone"):
            print("I win")
            i+=1
            
        elif (x=="stone" and random_choice=="scissor"):
            print("you win")
            u+=1
        else:
             print("tie")
             print(f"{x}")

print("Computers total score",i)
print("yours total score",u)
if(i>u):
            print("I win")

            
else:
    print("u win")



