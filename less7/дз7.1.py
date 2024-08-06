import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {
              execution_time:.9f} секунд.")
        return result

    return wrapper

# Пример использования


@measure_execution_time
def example_function():

    x = 20
    y = 30
    z = x + y
    print("Функция выполнена", z)


example_function()


# def time_ofFunction(function):
#     def wrapped(*args, **kwargs):
#         start_time = time.perf_counter()
#         res = function(*args, **kwargs)
#         print(time.perf_counter() - start_time)
#         return res
#     return wrapped


# @time_ofFunction
# def func(first, second):
#     return bin(int(first, 11) + int(second, 11))


# print(func("01", "01"))
