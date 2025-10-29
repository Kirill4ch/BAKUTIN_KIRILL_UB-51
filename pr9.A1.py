def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n-1)
x, n = int(input()), int(input())
print(x**n / faktorial(n))
