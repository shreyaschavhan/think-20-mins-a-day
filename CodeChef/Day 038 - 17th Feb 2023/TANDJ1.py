# cook your dish here
# https://www.codechef.com/LP1TO201/problems/TANDJ1

for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    difference = abs(c-a) + abs(d-b)
    if k == difference:
        print('YES')
    elif k > difference:
        if (k-difference) % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
            