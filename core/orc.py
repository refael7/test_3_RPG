import random

from core.player import Player
from game import Game
class Orc:
    def __init__(self):
        self.name = "monster"
        self.hp = 50
        self.type="orc"
        self.speed = random.randrange(0, 5)
        self.power = random.randrange(10, 15)
        self.armor_rating = random.randrange(2, 8)
        self.weapon="סכין"

    def speak(self):
        print(f"the type is:{self.type} the name is:{self.name}")

    def attack(self):
        # p = Player()
        # j = Game()
        # monster = j.choose_random_monster()
        # round2 = random.randrange(0, 20) + monster.speed
        # print(f"סכום הנקודות של השחקן מהסיבוב הזה{round2}")
        # if round2 > p.armor_rating:
        #     power = monster.power
        #     p.hp -= power
        # else:
        #     print( "המפלצת הפסידה התור עובר לשחקן")


        pass