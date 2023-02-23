# cook your dish here
# https://www.codechef.com/LP1TO205/problems/PERMEXIS

for _ in range(int(input())):
    N = int(input())
    A = set(map(int, input().split()))
    mini, maxi = min(A), max(A)
    if (maxi - mini) == (len(A) - 1):
        print('YES')
    else:
        print('NO')
    
    
    