# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (num и y).

num = int(input("Введите четверть: "))
if num == 1:
    print(f'{num}-> x>0;y>0')
elif num == 2:
    print(f'{num}-> x>0;y<0')
elif num == 3:
    print(f'{num}-> x<0;y<0')
elif num == 4:
    print(f'{num}-> x<0;y>0')
else:
    print("Ошибка, неправильная четрверь")

