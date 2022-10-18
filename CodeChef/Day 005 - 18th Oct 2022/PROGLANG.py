# proglang

for _ in range(int(input())):
    a, b, a1, b1, a2, b2 = [int(x) for x in input().split()]
    language1 = [a1, b1]
    language2 = [a2, b2]

    if a in language1 and b in language1:
        print(1)
    elif a in language2 and b in language2:
        print(2)
    else:
        print(0)
