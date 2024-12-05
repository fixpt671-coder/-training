class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    _file_name = "products.txt"

    def get_products(self):
        file = open(self._file_name, 'r')
        return file.read()
        file.close()

    def add(self, *products):
        for prod_name in products:
            file = open(self._file_name, 'a')
            if str(prod_name) not in self.get_products():
                file.write(str(prod_name) + '\n')
                file.close()
            else:
                print(f"Продукт {prod_name.name} уже есть в файле")

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

