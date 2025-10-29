matr = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
for i in matr:
    print(i)
def sumSD(matr):
    sum = 0
    for i in range(len(matr) - 1):
        sum += matr[i+ 1][i + 1]
    return(sum)

print(sumSD(matr))