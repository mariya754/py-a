#Свойтсво закрытый метод


class Critter(object):
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print('Общее число зверюшек', Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Обьект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans

    def __pass_time(self):
        self.hunger += 1
        self.boredom +=1

    @property
    def name(self):
        return self.__name

    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
           m = "прекрасно"
        elif 5 <= unhapiness <= 10:
            m = "неплохо"
        elif 11 <= unhapiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    print("Создание зверюшек.")
    crit1 = Critter('Зверюшка 1')
    crit2 = Critter('Зверюшка 2')
    crit3 = Critter('Зверюшка 3')

    Critter.status()

    crit1.talk()
    crit2.eat()
    crit3.play()
    print(crit1.mood)

main()