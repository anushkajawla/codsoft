#contact book
#stores name,phone no,email,address
#add contact
#view contact
#search contact
#update contact
#delete contact
import string
print("****************************************************")
print("_____________________________________________________")
print(" C O N T A C T                   B O O K              ")
print("****************************************************")
print("_____________________________________________________")


print("What function would you like to perform ?\n")

print("1. Add a contact")
print("2. Search contact")
print("3. Update contact")
print("4. Delete contact")
print("5. view contact")
print("6. Exit")

name=["anushka","aryan"]
phone=[7451,9759]
email=["as@gmail.com","aj@gmail.com"]
address=["rke","dli"]

def add_contact():
 
 na= input("Enter your name\n")
 name.append(na)
 n=(input("Enter your no\n"))
 phone.append(n)
 em=(input("Enter your email\n"))
 email.append(em)
 ad=(input("Enter your address\n"))
 address.append(ad)
 
def search_contact():
    searc=input("Enter the name of contact to be searched\n")
    if searc in name:
      print("found!!")
    else:
     print("not found")

     ask=input("do you wish to continue....enter y\n")
     if ask == 'y':
       searc1=input("Enter the phone no. of contact to be searched\n")
       if searc1 in phone:
        print("found!!")
       else:
        print("not found")   
    
        
    ask1=input("do you wish to continue....enter y\n")
    if ask1 == 'y':
       searc2=input("Enter the email of contact to be searched\n")
       if searc2 in phone:
        print("found!!")
       else:
        print("not found")   
    
    ask2=input("do you wish to continue....enter y\n")
    if ask2 == 'y':
       searc3=input("Enter the address of contact to be searched\n")
       if searc3 in phone:
        print("found!!")
       else:
        print("not found")   
   
     
def update_contact():
    change=input("input the name you wish to replace\n")
    changee=input("input the new name\n")
    if change in name:
        index=name.index(change)
        name[index] = changee
    else:
        print("not found")
    askk1=input("do you wish to continue....enter y\n")
    if askk1 =='y':
     change1=input("input the number you wish to replace\n")
     change1e=input("input the new number\n")
     if change1 in phone:
        index=phone.index(change1)
        phone[index] = changee1
     else:
        print("not found")
    askk2=input("do you wish to continue....enter 'y' if you do\n")
    if askk2 =='y': 
     change2=input("input the email you wish to replace\n")
     changee2=input("input the new email\n")
     if change2 in email:
        index=email.index(change2)
        email[index] = changee2
     else:
        print("not found")
    
   
    askk3=input("do you wish to continue....enter y\n")
    if askk3 =='y':
     change3=input("input the address you wish to replace\n")
     changee3=input("input the new address\n")
    if change in address:
        index=address.index(change3)
        address[index] = changee3
    else:
        print("not found")
      
 
def delete_contact():
 n1=input("Enter the name you wish to delete\n")
 if n1 not in name:
     print("not found")
 else:
     name.remove(n1)
 n2=input("Enter the phone no. you wish to delete\n")
 if n2 not in name:
     print("not found")
 else:
     phone.remove(n2)
 n3=input("Enter the email you wish to delete\n")
 if n3 not in name:
     print("not found")
 else:
     email.remove(n3)
 n4=input("Enter the address you wish to delete\n")
 if n4 not in name:
     print("not found")
 else:
     address.remove(n4)
def view_contact():
 print("The names are:",name)
 print("The phone no. are:",phone)
 print("The email address are:",email)
 print("The addresses present are:",address)

while(True):
 key =int(input("Press the corresponding key\n"))
 if(key == 1):
    add_contact()
 elif(key== 2):
     search_contact()
 elif(key== 3):
     update_contact()
 elif(key==4):
     delete_contact()
 elif(key==5):
      view_contact()

 elif(key==6):
      print("THANK YOU")
      break
