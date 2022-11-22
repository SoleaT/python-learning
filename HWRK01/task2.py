# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def assignValue(value):
    return int(value) == 1 or False

x=assignValue(input('Введите х (0 или 1): '))
y=assignValue(input('Введите y (0 или 1): '))
z=assignValue(input('Введите z (0 или 1): '))

print(f'Полученные предикаты: {x}, {y}, {z}')
print('Результат - ' + str(not (x and y and z) == ((not x) or (not y) or (not z))))

