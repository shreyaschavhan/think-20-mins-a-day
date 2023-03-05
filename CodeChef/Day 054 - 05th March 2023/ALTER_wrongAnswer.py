# cook your dish here


for _ in range(int(input())):
    A, B, P, Q = map(int, input().split())
    maxx = max(P/A, Q/B)
    minn = min(P/A, Q/B)
    if minn + 1 == maxx or minn == maxx:
        print('YES')
    else:
        print('NO')