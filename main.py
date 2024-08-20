class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(self.name, ' снесён, но он останется в истории')








h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Горный', 20)
h3 = House('ЖК Академический', 20)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h3.name, h3.number_of_floors)
del h2
del h3
print(House.houses_history)

