# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите х (0 или 1): ')) == 1 or False
y = int(input('Введите y (0 или 1): ')) == 1 or False
z = int(input('Введите z (0 или 1): ')) == 1 or False
print(f'Полученные предикаты: {x}, {y}, {z}')
print('Результат - ' + str(not (x and y and z) == ((not x) or (not y) or (not z))))
