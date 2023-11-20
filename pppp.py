
print("_____________________________________________________________________")
print("_____________________________________________________________________")
print("_____________________________________________________________________")
print("R O C K     P A P E R      S C I S S O R S       G A M E  !!!         ")
print("_____________________________________________________________________")

print("IMPORTANT: INSTRUCIONS")

print("You need to choose rock/ paper/scissors and the computer will choose a")
print("random option and you may will based on your luck!")
print("\n")
import random
ques=int(input("How many times do you wanna play?\n"))
for i in range(ques):

 choice =input("Choose either rock,paper or scissors \n")
 print("\n")
 print("The computer decides...")
 choicce=["rock","paper","scissors"]
 computer= random.choice(choicce)
 print("\n")
 print("You chose",choice)
 print("computer chose",computer)
 
 if choice == "paper":
    if computer == "paper":
        print("TIE")
    elif computer == "rock":
        print("YOU WIN <3")
        
    else:
        print("YOU LOST :(")
        
 elif choice == "rock":
    if computer == "rock":
        print("TIE")
    elif computer == "paper":
        print("YOU WIN <3")
        
    else:
        print("YOU LOST :(")
    
 if choice == "scissors":
    if computer == "scissors":
        print("TIE")
    elif computer == "rock":
        print("YOU WIN <3")
        
    else:
        print("YOU LOST :(")
 print("_____________________________________________________________________")
print("_____________________________________________________________________")       




      
