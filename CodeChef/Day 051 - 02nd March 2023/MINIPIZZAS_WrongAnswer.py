# cook your dish here


for _ in range(int(input())):
    N, K = map(int, input().split())
    if N == K:
        print(1)
    elif N < K:
        if K % N == 0:
            print(1)
        else:
            print(N)
    else:
        if N % K == 0:
            print(N//K)
        else:
            print(N)
