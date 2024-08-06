import time


start_time = time.time()  # время начала выполнения


def calculation():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError("Ошибка: деление на ноль"):
                print("error")
        else:
            result = "Ошибка: неверная операция!"
        print(f"{result}")

    except ValueError:
        print("Ошибка: введено не число!")


calculation()
end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time:.11f} секунд")
