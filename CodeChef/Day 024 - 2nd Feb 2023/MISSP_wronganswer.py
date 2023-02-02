# cook your dish here

for _ in range(int(input())):
    dolls = {}
    for __ in range(int(input())):
        typee = int(input())
        if typee in dolls:
            dolls[typee] += 1
        else:
            dolls[typee] = 1

    print(sorted(dolls.items(), key = lambda x:x[1])[0][0])
