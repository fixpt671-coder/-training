numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while i < len(numbers):
    if numbers[i] > 0:
        print(numbers[i])
        i += 1
    elif numbers[i] == 0:
        i += 1
    else:
        break
