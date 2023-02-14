# https://www.codechef.com/LP1TO201/problems/SMOL
# cook your dish here

for _ in range(int(input())):
    N, K = map(int, input().split())
    if K != 0:
        print(N % K)
    else:
        print(N)
