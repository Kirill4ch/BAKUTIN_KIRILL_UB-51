def factorial(n):
    f = 1
    for i in range(1, n):
        f *= i
    return f;

print(factorial(int(input())))