import random
from game import Game
class Player:
    def __init__(self):
        self.name="refael"
        self.hp=50
        self.speed=random.randrange(5,10)
        self.power=random.randrange(5,10)+2
        self.armor_rating=random.randrange(5,15)
        self.profession="לוחם"
    def speak(self):
        print(f"the player name is:{self.name}")
    def attack(self):
        # p=Player()
        # j=Game()
        # monster=j.choose_random_monster()
        # round1 = random.randrange(0, 20) + p.speed
        # print(f"סכום הנקודות של השחקן מהסיבוב הזה{round1}")
        # if round1 > monster.armor_rating:
        #     power = p.power
        #     print(f" הכוח של השחקן {power}")
        #     monster.hp -= power
        # else:
        #     round1 = "השחקן הפסיד התור עובר למפלצת"
        pass


