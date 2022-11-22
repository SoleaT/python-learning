# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
while True:
    try:
        x, y = int(input('Введите x: ')), int(input('Введите y: '))
        break
    except ValueError:
        print('Что-то пошло не так. Введите данные заново')
if x>0 and y>0:
    print("I четверть")
elif x>0 and y<0:
    print("IV четверть")
elif x<0 and y<0:
    print("III четверть")
elif x<0 and y>0:
    print("II четверть")
else:
    print('Как ты сюда попал??')