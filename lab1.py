print("Введите коэффициенты квадратного уравнения вида: a*x^2 + b*x + c")
a = float(input())
b = float(input())
c = float(input())
x1 = 0
x2 = 0
if a == 0:
    x1 = (-1) * c / b
    x2 = x1
else:
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print("Уравнение не имеет корней:(")
        exit()
    elif d == 0:
        x1 = (-1 * b) / (2 * a)
        x2 = x1
    else:
        x1 = (- 1 * b - (d ** (1/ 2))) / (2 * a)
        x2 = (- 1 * b + (d ** (1 / 2))) / (2 * a)
if x1 == x2:
    print("Корень уравнения:", x1)
else:
    print("Первый корень уравнения:", min(x1, x2))
    print("Второй корень уравнения:", max(x1, x2))