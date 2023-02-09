# cook your dish here

for _ in range(int(input())):
    X, Y, A = map(int,input().split())
    if A >= X and A < Y:
        print("YES")
    else:
        print("NO")
    
