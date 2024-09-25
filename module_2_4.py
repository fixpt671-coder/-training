numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    del_cnt = 0
    for j in range(len(numbers)):
        if numbers[i] % numbers[j] == 0:
            del_cnt += 1
        if del_cnt > 2:
            break
    if del_cnt == 2:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Простые", primes)
print("Не простые", not_primes)