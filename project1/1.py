class Critter:
    """Виртуальный питомец"""
    total = 0
    food = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)
    def food_choice():
        Critter.food += int(input('How much?'))

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("Меня зовут", self.name)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()


    def eat(self, food = 0):
        print("Мррр...  Спасибо!")
        self.hunger -= Critter.food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, play = 4):
        print("Уиии!")
        self.boredom -= play
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

    
    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()

        # кормление зверюшки
        elif choice == "2":
         crit.food_choice()
         crit.eat()
         

        # игра со зверюшкой
        elif choice == "3":
         crit.play()

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

main()