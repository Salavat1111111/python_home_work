#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print("Всего в неделе 7 дней : понедельник, вторник, среда, четверг, пятница, суббота, воскресенье")

number1 = int(input('Введите день недели: '))

if number1 == 6 : print("Да,сегодня суббота, гуляем.")
elif number1 == 7: print("Уже воскресенье, пора готовиться к рабочей неделе.")
elif number1 == 5: print("Ура, пятница. Начнем веселье.")
elif number1 == 4: print("четверг.")
elif number1 == 3: print("среда.")
elif number1 == 2: print("вторник.")
elif number1 == 1: print("И снова понедельник.")
else: print("Всего 7 дней в неделе. Давай сначала")