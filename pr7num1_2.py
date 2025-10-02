mas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 12, 234, 234, 234, 234, 234]
mas2 = [3, 13, 134, 123, 13, 43, 12, 432]
mas3 = [123, 12343, 4534, 65754, 345345, 345233, 765]

maso, NumMas = [mas1, mas2, mas3], 0
for i in maso:
    NumMas += 1
    if len(i) <= 15:
        print("Сумма элементов массива №"+ str(NumMas) + ": "+ str(sum(i)))
        print("Среднее арифметическое массивa №"+ str(NumMas)+ ": " + str(sum(i)/len(i)))
    else:
        print("Массив №" + str(NumMas) + " не подходит по условию")