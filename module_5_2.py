class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(*[i for i in range(1, new_floor + 1)])
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {len(self)}"

home = House("Урицкого 48", 666)
home.go_to(66)
print(str(home))