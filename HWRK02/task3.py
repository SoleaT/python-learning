# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

lst = {i: round((1 + (1 / i)) ** i, 2) for i in range(1, int(input('Введите цифру: ')) + 1)}
print('Значения:',lst)
print('Сумма значений:',sum(lst.values()))
