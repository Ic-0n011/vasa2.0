import os
from random import randint, choice

class mama:
    def __init__(self, name) -> None:
        self.name = name
        self.hp = 10
        self.max_hp = 10
        self.attack = 0
        self.deffend = 0
        self.mana = 0
        self.money = 100

        self.inventory = []
    
    def spend_hp(self, damages):
        damage = (self.defend - damages)
        if damage > 0:
            self.hp -= damage
        if self.hp <= self.max_hp:
            print("тут игра должна закончиться")
    
    def replenishment_mana(mana_plus):
        self.mana =+ mana_plus
    
    def show_hero(self) -> None:
        print("имя:", self.name)
        print("здоровье:", self.hp, "/", self.max_hp)
        print("мана:", self.mana)
        print("атака:", self.attack)
        print("защита:", self.deffend)
        print("деньги:", self.money)
        print("")


    def buy_item(self, price: int, item: str) -> None:
        """
        Покупает предмет item за price монет и кладет его в инвентарь героя
        """
        os.system("cls")
        if self.money >= price:
            self.money -= price
            self.inventory.append(item)
            print(f"{self.name купил {item} за {price} монет!")
        else:
            print(f"У {self.name} нет столько монет! Не хватило {price - self.money}")
        input("\nНажмите ENTER чтобы продолжить ")


    def consume_item(hero: list, idx: str) -> None:
        """
        Удаляет предмет из инвентаря по индексу и дает герою эффект этого предмета
        """
        if idx <= len(self.inventory) - 1 and idx > -1:
            print(f"{self.name} употребил {self.inventory[idx]}")
            if self.inventory[idx] == "зелье":
                self.hp += 10
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
            elif self.inventory[idx] == "яблоко":
                pass
            else:
                print("Никакого эффекта")
            self.inventory.pop(idx)
        else:
            print("Нет такого индекса!")
        print("")


    def play_dice(hero: list, bet: str) -> None:
        """
        Ставка от 1 монеты до количества монет героя
        Игрок и казино бросаю кости, кто больше, то забирает ставку
        TODO: Как удача влияет на кости?
        """
        try:
            bet = int(bet)
            except ValueError:
            print("Ставка недопустима")
        else:
            if bet > 0:
                if self.money >= bet:
                    hero_score = randint(2, 12)
                    casino_score = randint(2, 12)
                    print(f"{self.name} выбросил {hero_score}")
                    print(f"Трактирщик выбросил {casino_score}")
                    if hero_score > casino_score:
                        self.money += bet
                        print(f"{self.name} выиграл {bet} монет")
                    elif hero_score < casino_score:
                        self.money -= bet
                        print(f"{self.name} проиграл {bet} монет")
                    else:
                        print("Ничья!")
                else:
                    print(f"У {self.name} нет денег на такую ставку!")
            else:
                print("Ставки начинаются от 1 монеты!")



        input("\nНажмите ENTER чтобы продолжить")


    def combat_turn(attacker, defender):
        if attacker[1] > 0:
            damage = attacker[6]
            defender[1] -= damage
            print(f"{attacker[0]} ударил {defender[0]} на {damage} жизней!")


    def start_fight(hero: list) -> None:
        """
        Зависит ли враг от уровня героя?
        Формула аткаи и защиты?
        Можно ли выпить зелье в бою?
        """
        enemy = make_hero(hp_now=30, xp_now=123, inventory=["вражеский меч", "вражеский конь"])
        while self.hp > 0 and enemy[1] > 0:
            os.system("cls")
            combat_turn(hero, enemy)
            combat_turn(enemy, hero)
            print("")
            show_hero(hero)
            show_hero(enemy)
            input("\nНажмите ENTER чтобы сделать следующий ход")
        count_fight_result(hero, enemy)


    def count_fight_result(hero, enemy):
        os.system("cls")
        if self.hp > 0 and enemy[1] <= 0:
            print(f"{self.name} победил и получает в награду:")
            self.money += enemy[9]
            print(enemy[9], "монет")
            print("и предметы: ", end="")
            for item in enemy[10]:
                print(item, end=", ")
            self.inventory += enemy[10]
            levelup(hero)
        elif self.hp <= 0 and enemy[1] > 0:
            print(f"{enemy[0]} победил!")
            print("Игра должна закончиться тут!")
        else:
            print(f"{self.name} и {enemy[0]} пали в бою:(")
            print("Игра должна закончиться тут!")


    def choose_option(hero: list, text: str, options: list) -> int:
        """
        Показывает описание ситуации
        Показывает варианты
        Получает ввод пользователя
        Проверяет ввод и возвращает его, если он есть в вариантах
        """
        os.system("cls")
        show_hero(hero)
        print(text)
        for num, option in enumerate(options):
            print(f"{num}. {option}")
        option = input("\nВведите номер варианта и нажмите ENTER: ")
        try:
            option = int(option)
        except:  # выполнится, если try не получится
            print("Ввод должен быть целым неотрицательным числом")
        else:  # выполнится, если try удался
            if option < len(options) and option > -1:
                return option
            else:
                print("Нет такого выбора")


    def visit_hub(hero):
        text = f"{self.name} приехал к Хаб, здесь есть чем заняться:"
        options = [
            "заглянуть в лавку алхимика",
            "пойти в казино",
            "выйти в главное меню",
        ]
        option = choose_option(hero, text, options)
        os.system("cls")
        if option == 0:
            return visit_shop(hero)
        elif option == 1:
            return visit_casino(hero)
        elif option == 2:
            print("ушел в меню -почти-")
        elif option == 3:
            consume_item(hero, 0)
        input("\nНажмите ENTER чтобы продолжить")


    def visit_shop(hero:list) -> None:
        text = f"{self.name} приехал в лавку алхимика. здесь странно пахнет и продаются зелья. "
        options = ["купить зелье лечения за 10 монет",
            "купить зелье опыта ха 30 монет",
            "выйти из лавки в хаб",
            ]
        option = choose_option(hero, text, options)
        if option == 0:
            buy_item(hero, 10, "зелье лечение")
            return visit_shop(hero)
        elif option == 1:
            buy_item(hero, 30, "зелье опыта")
            return visit_shop(hero)
        elif option == 2:
            return visit_hub(hero)
        input("\nНажмите ENTER чтобы продолжить ")


    def visit_casino(hero: list) -> None:
    text = f"{self.name} приехал в казино. за вами следят охраники. "
    options = ["сесть за ближайший стол",
        "выйти из лавки в хаб",
        ]
    option = choose_option(hero, text, options)
    if option == 0:
        print("вы сели за стол")
        bet = input("Выберите ставку: ")
        return play_dice(hero, bet)
    elif option == 1:
        return visit_hub(hero)
        
    input("\nНажмите ENTER чтобы продолжить ")