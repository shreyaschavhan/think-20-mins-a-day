# cook your dish here
# https://www.codechef.com/LP1TO205/problems/MXMTRIO

for _ in range(int(input())):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    print((A[-1]-A[0]) * A[-2])
    