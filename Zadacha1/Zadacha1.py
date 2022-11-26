#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#  Пример:
#  - 6 -> да
#  - 7 -> да
#  - 1 -> нет
while True:
    input_day_num = input("Введите целое число от 1 до 7: ")
    if not input_day_num.isnumeric():
        print("Вы ввели не число, либо оно не целое. Попробуйте снова: ")
    elif not 1 <= int(input_day_num) <= 7:
        print("Ваше число вне диапазона. Попробуйте снова")
    else:
        if int(input_day_num) == 6 or int(input_day_num)== 7:
            print("Это выходной день")
        elif 0 < int(input_day_num) < 6:
            print("Это рабочий день")
        break





