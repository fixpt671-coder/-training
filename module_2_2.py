digit_1 = int(input("Введите число 1: "))
digit_2 = int(input("Введите число 2: "))
digit_3 = int(input("Введите число 3: "))

if digit_1 == digit_2 == digit_3:
    print(3)
elif digit_1 == digit_2 or digit_1 == digit_3 or digit_2 == digit_3:
    print(2)
else:
    print(0)
