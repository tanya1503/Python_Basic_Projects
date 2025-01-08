#Kaun Banega Karodpati
questions=[["In which programming language the fb was designed?","python","JS","PHP","None",2],

           ["In which programming language the fb was designed?","python","JS","PHP","None",2],

           ["In which programming language the fb was designed?","python","JS","PHP","None",2],

           ["In which programming language the fb was designed?","python","JS","PHP","None",2],

           ["In which programming language the fb was designed?","python","JS","PHP","None",2]]


levels=[1000,2000,5000,10000]
money=0


for i  in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]} is :")
    print(f"{question[0]}")
    print(f"a.{question[1]}   b.{question[2]}")
    print(f"c.{question[3]}   d.{question[4]}")


    reply = int(input("Enter your answer (1-4): "))
    if reply==3:
                  print(f"yeah!, this is a correct answer, you have won Rs.{levels[i]}")
    else:
                  print("Nah!,Thats a wrong answer")

                  break

              
          
          
          
          
