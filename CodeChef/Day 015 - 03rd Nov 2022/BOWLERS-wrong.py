# cook your dish here

for _ in range(int(input())):
    n, k, l = map(int, input().split())
    over = []
    for i in range(n):
        if k * l >= n:
            print(k - (i % k), end=' ')
        else:
            print("\n", -1)
            break
