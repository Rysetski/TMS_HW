input_str = input("Введите строчное значение: ")
choice = int(input("1 - Зашифровать, 2 - Расшифровать. Введите свой вариант: "))
pos_value = 3  # на сколько сдвигается значение символа

alpha_lower = 'defghijklmnopqrstuvwгдеёжзийклмнопрстуфхцчшщъы'
alpha_upper = alpha_lower.upper()
alpha_start = 'abcабв012'  # исключения для расшифровки
alpha_start_upper = alpha_start.upper()
alpha_start_summ = alpha_start + alpha_start_upper
alpha_number = '3456'
alpha_probel = ' '
alpha_exeption_eng_rus = 'xyzэюя'
alpha_exeption_upper = alpha_exeption_eng_rus.upper()
alpha_exeption_num = '789'
alpha_exeption = (alpha_exeption_eng_rus +
                  alpha_exeption_upper + alpha_exeption_num)  # все исключения xyzэюяXYZЭЮЯ789
# на  abcабвABCАБВ012 всё нормально
# меняется  с шагом 3 (цезаря)
alpha_zamena_exeption = 'abcабвABCАБВ012'
alpha_absolut = alpha_lower + alpha_upper + \
    alpha_number

if choice == 1:
    def func_coding(input_str, pos_value):
        new_str = ''
        for i in input_str:
            if i in (alpha_absolut + alpha_start_summ):
                new_str += chr(ord(i) + pos_value)
            elif i in alpha_probel:
                new_str += i
            elif i in alpha_exeption:
                index = alpha_exeption.index(i)
                new_str += alpha_zamena_exeption[index]
            else:
                print("Fatal error: недопустимый символ", i)
                return None
        return new_str

    result = func_coding(input_str, pos_value)
    if result is not None:
        print(result)

elif choice == 2:
    def func_decoding(input_str, pos_value):
        new_str = ''
        for i in input_str:
            if i in (alpha_absolut + alpha_exeption):
                new_str += chr(ord(i) - pos_value)
            elif i in alpha_zamena_exeption:
                index = alpha_zamena_exeption.index(i)
                new_str += alpha_exeption[index]
            elif i in alpha_probel:
                new_str += chr(ord(i))
            else:
                print("Fatal error: недопустимый символ", i)
                return None
        return new_str

    result = func_decoding(input_str, pos_value)
    if result is not None:
        print(result)

else:
    print("Таких символов программа не знает")
