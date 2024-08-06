from math import sqrt, pow, cos, sin, pi

# formula 1

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# x = int(input("Enter x: "))
# y = (
#     (pow(a, 2) / 3)
#     + ((pow(a, 2) + 4) / b)
#     + ((sqrt(pow(a, 2) + 4)) / 4)
#     + (sqrt(pow(pow(a, 2) + 4, 3)) / 4)
# )
# print(y)

# formula 2
# y = (pow(cos(pow(x, 2)), 2) + pow(sin(2 * x - 1), 2)) ** (1 / 3)

# print(y)


# formula 3
# y = cos(x) + sin(x)
# print(y)


# formula 4
# у = 5 * x + (3 * pow(x, 2)) * (sqrt(1 + (pow(sin(x), 2))))
# print(y)


# formula 5
# i = float(input("enter i: "))
# s = int(input("enter s: "))
# n = int(input("enter n: "))
# p = i / n

# m = (s * p * pow((1 + p), n)) / (pow((1 + p), n) - 1)

# print("Month payment: ", m)
# print("Total sum: ", m * n)
# print("Overpayment: ", (m * n) - s)


# formula 6

R1 = int(input("first planet R1: "))
v1 = float(input("first planet v1: "))
R2 = int(input("second planet R2: "))
v2 = float(input("second planet v2: "))

L1 = round((2 * R1 * pi) / v1, 5)
L2 = round((2 * R2 * pi) / v2, 5)

print(
    f"""
        Lenght of year on first planet {L1}
        Lenght of year on first planet {L2}
       Is lenght of year on first planet longer, then second? {L1 > L2}
       """
)
