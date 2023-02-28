# cook your dish here
# https://www.codechef.com/LP1TO205/problems/REVSORT

for _ in range(int(input())):
    N, X = map(int,input().split())
    A = list(map(int, input().split()))
    current = 0
    flag = 1
    for i in range(N):
        if current > A[i] and current + A[i] > X:
            flag = 0 
        current = max(current, A[i])
    
    if flag:
        print('YES')
    else:
        print('NO')
    