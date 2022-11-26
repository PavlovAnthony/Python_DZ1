# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
xp=[True, False]
yp=[True, False]
zp=[True, False]
for x in xp:
    for y in yp:
        for z in zp:
            print(f"X={x}, Y={y}, Z={z}")
            result1=(not(x or y or z))
            result2=(not x and not y and not z)
            print(f'значение равенства:{result1==result2}')
    