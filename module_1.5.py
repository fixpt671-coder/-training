# 2
immutable_var = ('1', "string", 1, True, list("Hello"))
print(immutable_var)

# 3
#immutable_var[0] = 21 #Ошибка, потому что кортеж не изменяемый объект
immutable_var[4].remove('o') #Нет ошибки, потому что мы изменяем другой объект, ссылка на который содержится в кортеже(т.е элемент кортежа никак не поменялся)
immutable_var = immutable_var + (1, 2)
print(immutable_var)

#4
mutable_list = ['1', "string", 1, True, list("Hello")]
mutable_list.append(321)
mutable_list[1] = mutable_list[1].upper()
mutable_list[-1] -= 21
print(mutable_list)