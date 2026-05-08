print("welcome to the bank")
print("-------------------------------------------------")
import random
import sys
bal = random.randint(200,1000)
print (bal)
choice = 0

def home():
    print("""
    1. Check Balance
        
    2. Deposit

    3. Withdraw

    4 Exit
    """)

    choice = int(input("What do you want to do today: "))

    if choice == 4:
        exsit()
        

    elif choice == 1:
        check_bal()
        question()
        

    elif choice == 2:
        print("How much would you like to deposit?")
        op()
        add()
        question()
        

    elif choice == 3:
        print("How much would you like to withdraw?")
        op()
        sub()
        question()
        

    else:
        print("Invalid choice")
        home()




def question():
    while True:
        ans = input("Would you like to go back to the home page? (yes/no): ").strip().lower()
        if ans == "y":
            home()
        elif ans == "n":
            exsit()
            
        elif ans == "yes":
            home()
        elif ans == "no":
            exsit()
            
        else:
            print("Please say yes or no")

def check_bal():
    print(f'Your balance is ${bal}')

def exsit():
     print ("Exsiting...")
     sys.exit()
        
def op():
    print('''
            1) 20            2) 50 
            
            3) 100           4) 150
                    5) Custom
        ''' )
    
        #here is asking what they want to do

def add():
    global bal
    print(f'Your balance is ${bal}')
    new = input("Enter here: ").strip().lower()
    if new == "5":
        print("How much would you like to deposite?")
        cus = int(input("Enter here: "))
        bal = bal + cus
        print(f'Your new balance is {bal}')
         #If they choose custom this is what we run

    elif new == "1": #option 1
        print("Adding 20...")
        bal += 20
        print(f'Your new balance is {bal}')

    elif new == "2": #option 2
        print("Adding 50...")
        bal = bal + 50
        print(f'Your new balance is {bal}')

    elif new == "3": #option 3
        print("Adding 100...")
        bal = bal + 100
        print(f'Your new balance is {bal}')
        
    elif new == "4": #option 4
        print("Adding 150...")
        bal = bal + 150
        print(f'Your new balance is {bal}')

def sub():
    global bal
    print(f'Your balance is ${bal}')

    new = int(input("Enter here: "))

    if new == 1:
        if bal < 20:
            print("You dont have enough funds")
        else:
            bal -= 20
            print(bal)

    elif new == 2:
        if bal < 50:
            print("You dont have enough funds")
        else:
            bal -= 50
            print(bal)

    elif new == 3:
        if bal < 100:
            print("You dont have enough funds")
        else:
            bal -= 100
            print(bal)

    elif new == 4:
        if bal < 150:
            print("You dont have enough funds")
        else:
            bal -= 150
            print(bal)

    elif new == 5:
        amt = int(input("How much are you withdrawing? "))

        if bal < amt:
            print("You dont have enough funds")
        else:
            bal -= amt
            print(bal)

home()