def custom_write(file_name : str, strings: list[str]) -> dict:
    string_positions = dict()
    string_num = 1
    file = open(file_name, 'w',  encoding = "utf-8")
    for string in strings:
        string_positions[(string_num, file.tell())] = string
        file.write(string + '\n')
        string_num += 1
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
