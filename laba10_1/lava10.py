
def matrica(file):
    matr = []
    with open(file, "r") as f:
        for line in f:
            linia = [int(x) for x in line.split()]
            matr.append(linia)
    return matr


def vivod(matr, name):
    f = open(name, "w")
    for line in matr:
        for w in line: 
            f.write(str(w) + " ")
        f.write('\n')


        

matrc = matrica('vvod.txt')
def sumSD(matr):
    sum = 0
    for i in range(len(matr) - 1):
        sum += matr[i][i + 1]
        file = open('vivod.txt', 'w')
        file.write(str(sum))


sumSD(matrc)
