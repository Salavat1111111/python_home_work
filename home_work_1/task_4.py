#Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

a = int(input('номер четверти от 1 до 4: ')) 
if a == 4:
    print('y положительное значение, x отрицательное значение')
elif a == 3:
    print('y отрицательное значение, x отрицательное значение')
elif a == 2:
    print('y отрицательное значение, x положительное значение')
elif a > 4:
    print("Такой четверти не сущевствует")
else:
    print('y положительное значение, x положительное значение')