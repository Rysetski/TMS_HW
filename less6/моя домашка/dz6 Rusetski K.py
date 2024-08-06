from random import choice

str = input("введите строчное значение, str = ")
choice = int(
    input("1 - Зашифровать, 2 - Рашифровать. Введите свой вариант, = "))
pos_value = 3       # на сколько сдвигается значение символа

alpha_lower = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзиклмнопрстуфхцчшщъыэюя1234567890'
alpha_upper = alpha_lower.upper()

if choice == 1:

    def func_coding(str, pos_value):

        new_str = ''

        for i in str:
            if i in alpha_lower:  # если не заглавная буква
                new_str += chr(ord(i) + pos_value)  # присвоить  индекс + 3
            elif i in alpha_upper:
                new_str += chr(ord(i) + pos_value)
            else:
                # для всего остального и цифр
                new_str += chr(ord(i) + pos_value)

        return new_str

    print(func_coding(str, pos_value))

elif choice == 2:

    def func_coding(str, pos_value):

        new_str = ''

        for i in str:
            if i in alpha_lower:
                new_str += chr(ord(i) - pos_value)
            elif i in alpha_upper:
                new_str += chr(ord(i) - pos_value)
            else:
                new_str += chr(ord(i) - pos_value)

        return new_str

    print(func_coding(str, pos_value))

else:
    print("таких символов программа не знает")
