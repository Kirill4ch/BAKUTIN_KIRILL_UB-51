matr = [[5, 2, 3, 1], [4, 2, 4, 1], [4, 32, 1, 5]]


for i in matr:

    i[i.index(max(i))], i[0] = i[0], i[i.index(max(i))]
    i[i.index(min(i))], i[-1] = i[-1], i[i.index(min(i))]
    print(i)