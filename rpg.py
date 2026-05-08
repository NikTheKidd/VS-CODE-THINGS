print("Welcome to RPG RANDOM")
print("----------------------")

player = 100
opp = 100
pots = 3



import random
import sys


def start_end():

    op = int(input("Type 1 or 2: "))
    if op == 2:
        exsit()
    elif op == 1:
        print("Running RPG GAME....")
        print() 
        print()
        print("User health: 100")
        print("You have now encountered a monster what choice do you want to choose? ")
        print("ennemy health: 100")
        menue()
        men_choose()


def men_choose():
    option = int(input("What would you like to chooes number 1-4?: "))
    
    if option == 1:
        attack()
    elif option == 2:
        heal()
    elif option == 3:
        stats()
    elif option ==4:
        run()
def menue():
    print("""
1) Attack

2) Heal         

3) check stats

4) Run        
          """)
    

#enemy attack
def enemy():
    global player
    dam = random.randint(5, 15)
    player = player - dam
    print("the enemy did", dam, "damage")
    print("Your new health is", player, "hp")



# attack , heal, check stats, and run
def attack():
    global opp
    dam = random.randint(10,25)
    print("You hit the enemy for", dam, "damage") 
    opp = opp - dam
    
    if opp <= 0:
        print()
        print()
        print()
        print ("enemy defeated you won the game..")
        start()
    else:
        print("enemys health is now", opp)
        enemy()
        menue()
        men_choose()

def heal():
    global player
    global pots
    heals = random.randint(15,25)
    
    if player >= 100:
        print("you can't heal your health is full")
        print("user health: ", player)
        menue()
        men_choose()
    else:
        enemy()
        pots -= 1
        print(f'You have {pots} healing pots left.')
        player = player + heals
        print("you healed for", heals, "hp")
        if player <= 100:
            print("you can't heal past 100")
            player = 100
            print("Your health is now:", player)
        else:
            print("Your health is now", player, "hp")
    
        menue()
        men_choose()

def stats():
    global player
    global opp
    global pots
    print("Your health is:", player,)
    print(f'You have {pots} healing potions left')
    menue()
    men_choose()

def run():
    print("You dont want to fight right now so lets go back to home")
    start()


#start and exsit
def start():
    print("""
1) Start

2) END
          """)
    start_end()
    
def exsit():
    print("Goodbye...")
    print("Exsiting....")
    sys.exit()







start()

    