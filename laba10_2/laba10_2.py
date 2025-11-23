def matrica(file):
    matr = []
    f = open(file, "r")
    for line in f:
        row = [int(x) for x in line.split()]
        matr.append(row)
    return matr

matr = matrica("vvod.txt")

zapis = open("vivod.txt", "w")

for i in matr:

    i[i.index(max(i))], i[0] = i[0], i[i.index(max(i))]
    i[i.index(min(i))], i[-1] = i[-1], i[i.index(min(i))]
    zapis.write(str(i) + "\n")
