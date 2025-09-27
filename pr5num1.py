

def countE(a):
    cnt = 0
    s = a.split()
    for i in s:
        if i[0] == "е" or i[0] == "Е":
            cnt += 1
    return cnt

print(countE(input()))
