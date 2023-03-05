# cook your dish here
# https://www.codechef.com/LP2TO301/problems/ALTER

for _ in range(int(input())):
    A, B, P, Q = map(int, input().split())
    maxx = max(P/A, Q/B)
    minn = min(P/A, Q/B)
    if ((minn + 1) == maxx or minn == maxx) and (P % A == 0 and Q % B == 0):
        print('YES')
    else:
        print('NO')