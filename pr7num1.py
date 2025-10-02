
import math

def rect(a, b):
    return a * b;

def triangle(a, b, c):
    return (a+b+c)/2;

def circle(diam):
    return (diam**2 * math.pi)


print("Выберете фигуру: \n1.Квадрат \n2.Треугольник \n3.Круг")
select = int(input())
if select == 1:
    print("Введите первую сторону")
    a = int(input())
    print("Введите вторую сторону")
    b = int(input())
    print("Площадь квадрата = " + str(rect(a, b)))
if select == 2:
    print("Введите первую сторону")
    a = int(input())
    print("Введите вторую сторону")
    b = int(input())
    print("Введите третью сторону")
    c = int(input())
    print("Площадь треугольника = " + str(rect(a, b, c)))
if select == 3:
    print("Введите диаметр круга")
    diam = int(input())
    print("Площадь круга = "+str(circle(diam)))