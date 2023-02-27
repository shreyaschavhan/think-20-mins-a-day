# cook your dish here
# https://www.codechef.com/LP1TO205/problems/REVSORT

for _ in range(int(input())):
    N, X = map(int,input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        if A[i] > A[i+1]:
            sum += A[i]
    if sum >= X:
        print('NO')
    else:
        print('YES')
