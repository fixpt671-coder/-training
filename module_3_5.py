def multiplied_digits(number):
    str_number = str(number)
    first_digit = int(str_number[0])
    if first_digit == 0:
        first_digit = 1
    if len(str_number) > 1:
        return first_digit * multiplied_digits(int(str_number[1:]))
    return first_digit

def multiplied_digits_2(number):
    last_digit = number%10
    next_number = number//10
    if last_digit == 0:
        last_digit = 1
    if next_number > 0:
        return last_digit*multiplied_digits(next_number)
    return 1

print(multiplied_digits(30), multiplied_digits_2(30))
