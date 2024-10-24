def test_function():
    def inner_function():
        print("Я в области видимости test_function")
    inner_function()
    return inner_function
test_function()
# inner_function()          Ошибка. Функция не определена
inner_function = test_function()
inner_function()
