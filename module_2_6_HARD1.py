
number = int(input("Введите число от 3 до 20: "))
pairs = [0] * 10000
result = ""
for i in range(1, number+1):
        for j in range(1, number+1):
                if number % (i + j) == 0 and pairs[int(str(i) + str(j))] == 0 and pairs[
                        int(str(j) + str(i))] == 0  and i != j:
                        result += str(i) + str(j)
                        pairs[int(str(i) + str(j))] += 1
print(result)
