import random
import string
len = int(input("Enter the Password length\n"))
print("Choose the number corresponding to the kind of password you like")
print("1-> NUMBERS")
print("2-> CHARACTERS")
print("3-> LETTERS")
print("4-> END")
passw = ""
 
while(True):
 choice = int(input("Pick a number \n"))
 if(choice == 1):
   passw += string.digits
 elif(choice == 2):
   passw+= string.ascii_letters
 elif(choice == 3):
  passw += string.punctuation
 elif(choice == 4):
      break
 else:
    print("Please pick a valid option!")

password = []
 
for i in range(len):
   
    key = random.choice(passw)
    password.append(key)
 

print("The random password is",password)

             
