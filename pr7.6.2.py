def S(st1, st2, st3, st4, diag):
    poluperim1 = (st1 + st2 + diag)/2
    poluperim2 = (st3 + st4 + diag)/2
    s1 = (poluperim1 * (poluperim1 - st1) * (poluperim1 - st2) * (poluperim1 - diag))**0.5
    s2 = (poluperim2 * (poluperim2 - st3) * (poluperim2 - st4) * (poluperim2 - diag))**0.5
    return(s1 + s2)

print(S(3, 4, 3, 4, 5))
