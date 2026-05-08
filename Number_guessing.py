


print("Welcome to the number guessing game!")
print("-------------------------------------")

print("What difficulty do you want?")
while True: #main menue
    atmp = 0
    difi = int(input("""
    1) Easy (1-10 5 attempts)            
                    
    2) Medium (1-50 7 attempts) 
                            
    3) Hard (1-100 10 attempts)   

    4) Exit     
                    
    Enter here: """))

    import random


#this is the exist
    if difi == 4:
        print("Exiting...")
        break




#this is easy mode
    if difi == 1:
        print("You chose easy mood PUSSY ")
        import random
        num = random.randint(1, 10)
        atmp = 1
        print(num) 
        while True:
            try:
                user = int(input("Take your guess (1-10): "))
                print(f'{atmp})')
            except ValueError:
                print("really nigga your done")
                print("Exiting")
                exit()

        
            #if they go more than they are supposed to
            if user > 10:
                print("really nigga your done")
                print("Exiting...")
                exit()

            if user == num:
                print("You got it!!!")
                #lay again
                ans = input("Would you like to play again? yes or no : ").strip().lower()
                if ans == "yes":
                    break
                else:
                    print("Exiting...")
                    exit()

            elif atmp > 4:
                print("YOU LOOSE!!!")
                #play again
                ans = input("Would you like to play again? yes or no : ").strip().lower()
                if ans == "yes":
                    break
                else:
                    print("Exiting...")
                    exit()
                
            
            elif user < num:
                print("Higher try again")
                atmp += 1
                
            
            elif user > num:
                print("Too high try again")
                atmp += 1
            
       
       
       
       #medium mode 
    elif difi == 2:
        print("You chose Medium mode ")
        import random
        num = random.randint(1, 50)
        atmp = 1
        print(num) 
        while True:
            try:
                user = int(input("Take your guess (1-50): "))
                print(f'{atmp})')
            except ValueError:
                print("Really nigga bye.")
                print("Exiting")
                exit()

            #if they go more than they are supposed to
            if user > 50:
                print("really nigga your done")
                print("Exiting...")
                exit()

            if user == num:
                print("You got it!!!")
               #play agin
                ans = input("Would you like to play again?yes or no : ").strip().lower()
                if ans == "yes":
                    break
                else:
                    print("Exiting...")
                    exit()
                

            elif atmp > 7:
                print("YOU LOOSE!!!")
                # play again
                ans = input("Would you like to play again? yes or no : ").strip().lower()
                if ans == "yes":
                    break
                else:
                    print("Exiting...")
                    exit()
            
            elif user < num:
                print("Higher try again")
                atmp += 1
                
            
            elif user > num:
                print("Too high try again")
                atmp += 1



#hard mode
    if difi == 3:
        print("You chose Hard mode ")
        import random
        num = random.randint(1, 100)
        atmp = 1
        print(num) 
        while True:
            try:
                user = int(input("Take your guess (1-100): "))
                print(f'{atmp})')
            except ValueError:
                print("Really nigga bye.")
                print("Exiting")
                exit()

            #if they go more than they are supposed to
            if user > 100:
                print("really nigga your done")
                print("Exiting...")
                exit()

            if user == num:
                print("You got it!!!")
                #play again
                ans = input("Would you like to play again? yes or no : ").strip().lower()
                if ans == "yes":
                    break
                else:
                    print("Exiting...")
                    exit()

            elif atmp > 10:
                print("YOU LOOSE!!!")
                #play again
                ans = input("Would you like to play again? yes or no: ").strip().lower()
                if ans == "yes":
                    break
                else:
                    print("Exiting...")
                    exit()
            
            elif user < num:
                print("Higher try again")
                atmp += 1
                
            
            elif user > num:
                print("Too high try again")
                atmp += 1