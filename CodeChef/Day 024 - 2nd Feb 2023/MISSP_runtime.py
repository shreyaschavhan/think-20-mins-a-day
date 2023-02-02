
for _ in range(int(input())):
    dolls = {}
    for __ in range(int(input())):
        typee = int(input())
        if typee in dolls:
            dolls[typee] += 1
        else:
            dolls[typee] = 1

    print(list(dolls.keys())[list(dolls.values()).index(1)])
