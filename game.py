from core.goblin import Goblin
from core.orc import Orc
from core.player import Player
import random

class Game:
    def start(self):
        self.show_menu()
        self.create_player()
        player=Player()
        player.speak()
        monster=self.choose_random_monster()
        monster.speak()
        self.battle(player,monster)

    def show_menu(self):
        word = input("האים אתה רוצה להמשיך במשחק כן או לא?")
        while word != "כן" and word != "לא":
            word = input("האים אתה רוצה להמשיך במשחק כן או לא?")
        if word=="כן":
            print("הקרב מתחיל")
        else:
           print("יציאה")

    def create_player(self):
        p=Player()
        return p
    def choose_random_monster(self):
        arr=[Orc,Goblin]
        number=random.randrange(0,2)
        a = arr[number]()
        return a

    def battle( self,player, monster):

        global attack,p
        player1=random.randrange(1,6)+player.speed
        monster1=random.randrange(1,6)+monster.speed
        print(f"מה שיצא לשחקן:{player1}")
        print(f"מה שיצא למפלצת:{monster1}")

        if player1>monster1:
            p=Player()
            p.attack()
            print("השחקן מתחיל לשחק")
            attack=1
        elif  monster1>player1:
            if monster==Orc:
                o=Orc()
                o.attack()
                print("המפלצת מתחילה לשחק")
                attack=2
            elif monster==Goblin:
                g = Goblin()
                g.attack()
                print("המפלצת מתחילה לשחק")

                attack = 2
        else :
            p=Player()
            p.attack()
            print("השחקן מתחיל לשחק")
            attack=1
        if attack==1:
          round1=random.randrange(0,20)+p.speed
          print(f"סכום הנקודות של השחקן מהסיבוב הזה{round1}")
          if round1>monster.armor_rating:
              power=p.power
              print(f" הכוח של השחקן {power}")
              monster.hp-=power
          else:
              round1="השחקן הפסיד התור עובר למפלצת"
        else:
            round2=random.randrange(0,20)+monster.speed
            print(f"סכום הנקודות של השחקן מהסיבוב הזה{round2}")
            if round2 > monster.armor_rating:
                power=monster.power
                p.hp-=power
            else:
                round2 = "השחקן הפסיד התור עובר למפלצת"

        # pass
game = Game()
# print(game.choose_random_monster())
game.start()







