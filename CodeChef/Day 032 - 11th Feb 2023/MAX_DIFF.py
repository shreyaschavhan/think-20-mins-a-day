# Problem: https://www.codechef.com/LP1TO201/problems/MAX_DIFF

for _ in range(int(input())):
    n, s = map(int, input().split())

    if s <= n:
        print(s)
    else:
        print((2*n) - s)
