print("****************************")
print("****************************")
print("____________________________")
print("____________________________")

print("C  A  L  C  U  L  A  T  O  R")
print("\n")
print("\n")
print("CHOOSE THE OPERATION YOU WISH TO PERFORM")
print("Press 1 for ADDITION")
print("Press 2 for SUBTRACTION")
print("Press 3 for MULTIPLICATION")
print("Press 4 for DIVISION")

print("\n")
num3 = float(input("Enter your choice:\n"))
print("\n")
num1 = float(input("Enter variable 1\n"))
print("\n")
print("Variable 1 is",num1)
print("\n")
num2 = float(input("Enter variable 2\n"))
print("\n")
print("Variable 2 is",num2)
print("\n")

if (num3 == 1):
    print("Sum is ",num1+num2)
elif (num3 == 2):
    print("Dfference is",num1-num2)
elif (num3 == 3):
    print("Product is", num1*num2)
elif (num3 == 4):
    if (num2 == 0):
      print("Invalid Entry")
    else:
      print ("Division is",num1/num2)
else:
    print("Invalid Entry")





print("________________________________")            
print("******************************")
print("******************************")
print("________________________________")          




