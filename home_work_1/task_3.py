# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

number1 = int(input("Введите корлинаты точки X: "))
number2 = int(input("Введите корлинаты точки Y: "))

if number1 > 1 and number2 > 1: print("Первая четверть")
elif number1 > 1 and number2 < -1: print ("Вторая четверть")
elif number1 < -1 and number2 < -1: print ("Третья четверть")
else : print("Четвертая четверть")

