# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def get_coord(v):
    while True:
        try:

            a, b = [float(s) for s in input(
                f'введите координаты точки {v} через пробел: ').split()]
            return a, b
        except ValueError:
            print("Ошибочный ввод.")


x, y = get_coord('A')
x1, y1 = get_coord('B')
res = ((x1-x)**2+(y1-y)**2)**0.5
print(f'Длина искомого отрезка : {round(res, 3)}')
