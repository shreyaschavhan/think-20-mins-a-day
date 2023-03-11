# cook your dish here
# https://www.codechef.com/LP2TO308/problems/SUBPERM

for _ in range(int(input())):
    N, K = map(int, input().split())
    
    if N == 1 and K == 1:
        print(1)
    elif N > 1 and K == 1:
        print(-1)
    else:
        for i in range(1, K):
            print(i, end=' ')
        for i in range(N, K-1, -1):
            print(i, end=' ')
        print()