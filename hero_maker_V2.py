#---------------------------
#Authour: Charlotte Cordwell
#Name: Hero_Maker
#Purpose: randomly creates a hero
import random

class  Hero:
    def __init__(self, name, pro, weapon, strength,agility,iq, magical_abi ):
        self.name = name
        self.health = 100
        self.pro= pro
        self.strength=strength
        self.agility = agility
        self.weapon = weapon
        self.iq = iq
        self.magical_abi = magical_abi
        

            
    def show_values(self):
        print("Name:",self.name)
        print("Health:", self.health)
        print("Profession:", self.pro)
        print("Weapon:", self.weapon)
        print("Strength:", self.strength)
        print("Agility:", self.agility)
        print("IQ:",self.iq)
        print("Magical Ability:",self.magical_abi)
        

PRO= ["Hero","Assasin", "Wizard","Ninja","Healer","Pirate"]

WEAPONS=["Sword", "Nunchucks", "Wand", "Rock", "Ax", "Rifle","Butter Kinfe","Bow and Arrow"]

MONSTERS = ["Miner 69er","Buger King Foot Lettuce", "The Byson", "MattyBRaps","Edwin","Logan Paul","Momo"]
MWEAPONS = ["Vlog Camera","Pool Noodle","Can of whoop ass","Fully grown cat", "Air Pods, Iphone XS, Apple Watch"]

def get_values():
    
    global name
    global pro
    global strength
    global agility
    global weapon
    global iq
    global magical_abi

    pro = PRO[random.randrange(0,len(PRO))]
    name = input("What is the Hero's name?")
    strength = random.randrange(1,100)
    agility = random.randrange(1,100)
    weapon = WEAPONS[random.randrange(0,len(WEAPONS))]
    iq = random.randrange(50,170)
    magical_abi = random.randrange(1,100)

def fight():
    monster = MONSTERS[random.randrange(0,len(MONSTERS))]
    mon_weapon = MWEAPONS[random.randrange(0,len(MWEAPONS))]
    mon_health = 2
    print("You have encountered",monster)
    choice = input("What do you do? 1. Fight 2.Run")
    if choice ==2:
        exit
    else:
        print("You fight",monster,"It pulls out a",mon_weapon)
        choice_2 = int(input("Do you: 1.Attack 2.Dodge 3.Block"))
    
    if choice_2 == 1:
        mon_health = mon_health-1
        print("You hit",monster,"With your",weapon)
        print(monster,":'OUCH THAT HURT'")
        print(monster,"'s health is now",mon_health)
    else:
        print ('ok')
        
        
        
    
    
get_values()              
hero1= Hero(name, pro,weapon, strength, agility,iq ,magical_abi)
hero1.show_values()
fight()





