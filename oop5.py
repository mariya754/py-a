#Свойтсво меня настроение
#Свойства

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
        print("Меня зовут", self.name)

def main():
    print("Создание зверюшек.")
    crit1 = Critter('Зверюшка 1')
    crit2 = Critter('Зверюшка 2')
    crit3 = Critter('Зверюшка 3')

    Critter.status()

    print('Доступ к свойству объекта:', crit1.mood)

main()