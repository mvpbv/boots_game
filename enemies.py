import time
from random import randint


class NormalEnemy:
    def __init__(self):
        self.names = ["Goblin", "Devilish Imp", "Evil Gnome", "Werewolf", "Ogre", "Vec"]
        self.name = self.names[randint(0, len(self.names)-1)] 
        self.hp = 30
        self.hp += randint(0, 2) * 5
        self.atk = 15
        self.death_quotes = ("Fuck you Boots, furry bastard",
                             "My friends will avenge me, bearman!",
                             "I hope you step on a bear trap",
                             "Furry wizard fuck")
        print(f"{self.name} APPEARS!")

    def buff_attack(self):
        print(f"{self.name} ATTEMPTS TO CAST -BUFF ATTACK-")
        time.sleep(1.5)
        flip = randint(0, 1)
        if flip == 0:
            print("SUCCESS")
            time.sleep(1.5)
            self.atk += 5
            print(f"{self.name} GETS +5 ATK")
            time.sleep(1.5)
        else:
            print("FAIL")
            time.sleep(1.5)

    def normal_atk(self, boots):
        buff = randint(0, 1)
        if buff == 0:
            self.buff_attack()
        print(f"{self.name} ATTACKS BOOTS FOR {self.atk} DMG")
        boots.hp -= self.atk

    def check_death(self):
        if self.hp <= 0:
            print(f"{self.name}: {self.death_quotes[randint(0, len(self.death_quotes)-1)]}")
            time.sleep(2)
            print(f"{self.name} DIES")
            time.sleep(2)
            return True
        return False
    
class BearMonk(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.name = "Bear Monk"
        self.hp = 50
        self.atk = 20
        print(f"{self.name} APPEARS!")

    def normal_atk(self, boots):
        buff = randint(0, 1)
        if buff == 0:
            self.buff_attack()
        print(f"{self.name} ATTACKS BOOTS FOR {self.atk} DMG")
        boots.hp -= self.atk 
        if randint(0, 1) == 0:
            self.heal()

    def heal(self):
        print(f"{self.name} HEALS FOR 10 HP")
        time.sleep(1.5)
        self.hp += 10
        if self.hp > 50:
            self.hp = 50

class BearAssassin(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.name = "Bear Assassin"
        self.hp = 50
        self.atk = 20
        print(f"{self.name} APPEARS!")

    def normal_atk(self, boots):
        self.buff_attack()
        print(f"{self.name} ATTACKS BOOTS FOR {self.atk} DMG")
        boots.hp -= self.atk

class Vec(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.name = "Vec"
        self.hp = 30
        self.atk = 15
        print(f"{self.name} APPEARS!")

    def normal_atk(self, boots):
        rand = randint(0, 4)
        if (rand == 0):
            self.bus(boots)
        elif (rand == 1):
            self.buff_attack()
        elif (rand == 2):
            self.report_casualties(boots) 
        else:
            if (randint(0, 1) == 0):
                self.buff_attack()
            print(f"{self.name} ATTACKS BOOTS FOR {self.atk} DMG")
            time.sleep(1.5)
            boots.hp -= self.atk
        

    def bus(self, boots):
        print(f"{self.name} summons a bus driving straight at Boots")
        time.sleep(1.5)
        print("Boots is hit by the bus")
        print(f"{self.name} attacks Boots for {self.atk * 2} DMG")
        boots.hp -= self.atk * 2

    def report_casualties(self, boots):
        print(f"{self.name}: @Boots @ChainsawMan I just want to let you guys know I just watched someone get hit by a bus")
        print(f"{self.name}: I literally watched them die and I didn't care")
        time.sleep(1.5)
        print(f"{self.name} ATTACKS BOOTS FOR {self.atk} DMG") 
        boots.hp -= self.atk * 3

class UndeadNormalEnemy:
    def __init__(self, name):
        if (name == "Vec"):
            self.name = f"Undead Nebulo"
        else:
            self.name = f"Undead {name}"
        self.quote = f"{self.name}: I serve Boots!"
