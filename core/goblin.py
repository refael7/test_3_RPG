import random
from game import Game
from core.player import Player


class Goblin:
    def __init__(self):
        self.name = "bob"
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randrange(5, 10)
        self.power = random.randrange(5, 10)
        self.armor_rating = random.randrange(2, 8)
        self.weapon = " חרב "

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
        #     round2 = "המפלצת הפסידה התור עובר לשחקן"
        pass

