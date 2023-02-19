# cook your dish here
# https://www.codechef.com/LP1TO205/problems/CM164364

for _ in range(int(input())):
    n, x = map(int, input().split())
    A = set(int(x) for x in input().split())
    if len(A) >= (n-x):
        print(n-x)
    else:
        print(len(A))
    
    