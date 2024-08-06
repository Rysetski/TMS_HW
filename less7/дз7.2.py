from functools import reduce
import time

# Данные о комнатах
rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]


# Функция для вычисления площади комнаты
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {
              execution_time:.15f} секунд.")
        return result

    return wrapper


def room_area(room):
    return room["length"] * room["width"]


# Используем map для вычисления площадей всех комнат
areas = map(room_area, rooms)


# Используем reduce для суммирования всех площадей
total_area = reduce(lambda x, y: x + y, areas)

print(f"Общая площадь квартиры: {total_area} кв.м")


# @measure_execution_time
# def example_function():

#     rooms = [
#         {"name": "Kitchen", "length": 6, "width": 4},
#         {"name": "Room 1", "length": 5.5, "width": 4.5},
#         {"name": "Room 2", "length": 5, "width": 4},
#         {"name": "Room 3", "length": 7, "width": 6.3},
#     ]


# def room_area(room):
#     return room["length"] * room["width"]


# areas = map(room_area, rooms)
# total_area = reduce(lambda x, y: x + y, areas)

# print(f"Общая площадь квартиры: {total_area} кв.м")

# print("Функция выполнена")


# example_function()
