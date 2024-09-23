# Словри
my_dict = {"Иван": 2004,
           "Артем": 1666}
print(my_dict)
print(my_dict["Артем"], my_dict.get("John"))
my_dict.update({"Саня": 988,
                "Женек": 20001})
print(my_dict.pop("Саня"))
print(my_dict)

# Множества
my_set = {True, False, True, False, 12, 21, 12, "set", "sad", "sad", (32, 23)}
print(my_set)
my_set.add("Уникальный")
my_set.add("Элемент")
my_set.remove(True)
my_set.discard(True)
ex_set = my_set.pop()
print(my_set)

