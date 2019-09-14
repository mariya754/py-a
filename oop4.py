#Свойство менять имя

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
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя зверюшки успешно изменено.")

    def talk(self):
        print("Меня зовут", self.name)

def main():
    print("Создание зверюшек.")
    crit1 = Critter('Зверюшка 1')
    crit2 = Critter('Зверюшка 2')
    
    Critter.status()

    print("Попытка изменить имя на Бобик")
    crit1.name = "Бобик"
    print("Имя зверушки:", crit1.name)

    print("Попытка изменить имя на пустую строку")
    crit2.name = ""
    print("Имя зверюшки:", crit2.name)
main()