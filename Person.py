import os
from random import randint, choice

class mama:
    def __init__(self) -> None:
        self.name = "mama"
        self.hp = 0
        self.max_hp = 0
        self.attack = 0
        self.deffend = 0
        self.mana = 0
        self.money = 0
        self.right_hand = []
        self.left_hand = []
        self.inventory = []
    
    def spend_hp(self, damages):
        damage = (self.defend - damages)
        if damage > 0:
            self.hp -= damage
        if self.hp <= self.max_hp:
            print("тут игра должна закончиться")
    
    def replenishment_mana(self, mana_plus):
        self.mana =+ mana_plus
    
    def show_hero(self) -> None:
        print("имя:", self.name)
        print("здоровье:", self.hp, "/", self.max_hp)
        print("мана:", self.mana)
        print("атака:", self.attack)
        print("защита:", self.deffend)
        print("деньги:", self.money)
        print("")


class Druid(mama):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    def gen(self):
        self.hp += 30
        self.max_hp += 30
        self.attack += 5
        self.deffend += 10
        self.mana += 100
        self.money += 50



class wielder_of_magic(mama):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    def gen(self):
        self.hp += 10
        self.max_hp += 15
        self.attack += 10
        self.deffend += 0
        self.mana += 500
        self.money += 10


class knight(mama):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    def gen(self):
        self.hp += 30
        self.max_hp += 30
        self.attack += 5
        self.deffend += 10
        self.mana += 20
        self.money += 50


p1 = wielder_of_magic("Фокусник")
p1.gen()
p1.show_hero()

p2 = knight("Жонглер")
p2.gen()
p2.show_hero()


def fight(p1, p2):
    print(" ")
    print("здоровье игрока ", p1.name, "; ", p1.hp, "/", p1.max_hp)
    print("здоровье игрока ", p2.name, "; ", p2.hp, "/", p2.max_hp)
    q = True
    while q:
        print("здоровье игрока ", p1.name, "; ", p1.hp, "/", p1.max_hp)
        print("здоровье игрока ", p2.name, "; ", p2.hp, "/", p2.max_hp)

        x = p1.deffend - p2.attack
        if x < 0:
            print("мимо")
            p1.hp += x
        print(x)
        x = p2.deffend - p1.attack
        if x < 0:
            print("мимо")
            p2.hp += x
        print(x)
        if p1.hp <= 0:
            print("игра оконченна игрок ", p1.name)
            q = False
        if p2.hp <= 0:
            print("игра оконченна игрок ", p2.name)
            q = False
        input()
    print(" ")



fight(p1, p2)

print("здоровье игрока ", p1.name, "; ", p1.hp, "/", p1.max_hp)
print("здоровье игрока ", p2.name, "; ", p2.hp, "/", p2.max_hp)