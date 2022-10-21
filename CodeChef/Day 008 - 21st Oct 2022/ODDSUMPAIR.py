# cook your dish here


for _ in range(int(input())):
    l = [int(x) for x in input().split()]
    countOdd = 0
    countEven = 0
    for i in l:
        if i % 2 == 0:
            countEven += 1

        else:
            countOdd += 1

    if countEven == 3 or countOdd == 3:
        print("NO")
    else:
        print("YES")
