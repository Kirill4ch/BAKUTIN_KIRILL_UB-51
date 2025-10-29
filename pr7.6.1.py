def evc(a, b):
    res = []
    if a > b:
        naib, naim = a, b
    else: naib, naim = b, a
    ostat = naib % naim
    while ostat != 0:
        ostat = naib % naim
        naib = naim
        naim = ostat
        res.append(naim)
    return res[-2]

def nok(a, b):
    return (a*b)/evc(a, b)

print(nok(12, 10))