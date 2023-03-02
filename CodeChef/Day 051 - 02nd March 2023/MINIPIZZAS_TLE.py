# cook your dish here


for _ in range(int(input())):
    N, K = map(int, input().split())
    i = 1
    while (i * K) % N:
        i += 1
    print(i)
