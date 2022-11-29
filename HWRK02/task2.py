# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from math import factorial
print([factorial(int(i)) for i in range(1,int(input('Введите число: ')))])

# \(°□° )/
# digit = int(input('Введите число: '))
# digits = list(range(1, digit))
# for i in range(1, len(digits)):
#     for j in range(1, i + 1):
#         digits[i] *= j
# print(digits)
