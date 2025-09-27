def AB(a, b):
    t = b - a
    for i in range(b - a + 1):
        print(b - t)
        t -= 1

print(AB(10, 20))
