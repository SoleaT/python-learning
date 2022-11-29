# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Способ1, Запись1
print('Сумма цифр:', sum(int(i) for i in input('Введите число: ') if i.isdigit()))

# :) Способ1, Запись2
s = input('Введите число: ')
sm = 0
for i in s:
    if i != '.' and i != ',':
        sm += int(i)
print('Сумма цифр:', sm)

# Способ2.

s = [int(i) for i in input('Введите число: ').split('.')]
sm = 0
for num in s:
    while num > 0:
        sm += num % 10
        num //= 10
print('Сумма цифр:', sm)
