# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def get_coord():
    while True:
        try:
            a, b = [float(s) for s in input(
                'введите координаты точки X и Y через пробел: ').split()]
            return a, b
        except ValueError:
            print("Ошибочный ввод.")


x, y = get_coord()
if x < 0 and y < 0:
    print(f"X: {x}, Y: {y}, 3-я четверть")
elif x > 0 and y < 0:
    print(f"X: {x}, Y: {y}, 4-я четверть")
elif x > 0 and y > 0:
    print(f"X: {x}, Y: {y}, 1-я четверть")
elif x < 0 and y > 0:
    print(f"X: {x}, Y: {y}, 2-я четверть")
elif x == 0 and y != 0:
    print(f"X: {x}, Y: {y}, ось Y")
elif y == 0 and x != 0:
    print(f"X: {x}, Y: {y}, ось X")
elif x == 0 and y == 0:
    print(f"X: {x}, Y: {y}, Центр")
