# cook your dish here
# https://www.codechef.com/LP2TO308/problems/MIXCOLOR


for _ in range(int(input())):
    N = int(input())
    A = set(map(int, input().split()))
    
    print(N - len(A))
    