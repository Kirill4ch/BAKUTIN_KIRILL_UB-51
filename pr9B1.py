def main():
    t = int(input())
    if t == 0:
        return 0
    else:
        mr = main()
        return max(t, mr)
