print("Welcome to the bank")
import random
balance = random.randint(200, 1000)
while True:
    print("-------------------------------------------------")

    print("""
    1. Check Balance
        
    2. Deposite

    3. Withdraw

    4 exist 
        """"")

    choice = int(input("What would you like to choose: "))

    if choice == 4:
        print("Existing...")
        break

    if choice == 1:
        print(f'Your balance is ${balance}')
        continue
    #here is just checking their balance

    elif choice == 2:
        print("How much would you like to deposite?")
        print('''
            1) 20            2) 50 
            
            3) 100           4) 150
                    5) Custom
            ''' )
        #here is asking what they want to do

        new = input("enter here: ").strip().lower()
        if new == "5":
            print("How much would you like to deposite?")
            cus = int(input("Enter here: "))
            balance = balance + cus
            print(f'Your new balance is {balance}')
            #If they choose custom this is what we run

        elif new == "1": #option 1
            print("Adding 20...")
            balance = balance + 20
            print(f'Your new balance is {balance}')

        elif new == "2": #option 2
            print("Adding 50...")
            balance = balance + 50
            print(f'Your new balance is {balance}')

        elif new == "3": #option 3
            print("Adding 100...")
            balance = balance + 100
            print(f'Your new balance is {balance}')
        
        elif new == "4": #option 4
            print("Adding 150...")
            balance = balance + 150
            print(f'Your new balance is {balance}')


    elif choice == 3: #chosing to withdraw
        print("How much would you like to withdraw?")
        print('''
            1) 20            2) 50 
            
            3) 100           4) 150
                    5) Custom
            ''' )
        new = int(input("Enter here: ")) #the input for options here
        if new == 1:
            if balance < 20:
                print("You dont have enough funds")
            else:
                balance -= 20
                print(balance)
        elif new == 2:
            if balance < 50:
                print("You dont have enough funds")
            else:
                balance -= 50
                print(balance)
        elif new == 3:
            if balance < 100:
                print("You dont have enough funds")
            else:
                balance -= 100
                print(balance)    
        elif new == 4:
            if balance < 150:
                print("You dont have enough funds")
            else:
                balance -= 150
                print(balance)
        elif new == 5: #had trouble here a lil bit  but this is the custom option
            print("How much are you withdrawing?")
            amt = int(input("Enter Here: "))
            if balance < amt:
                print("You dont have enough funds")
                print(f'Your balance is: ${balance}')
            else:
                balance = balance - amt
                print(balance)



