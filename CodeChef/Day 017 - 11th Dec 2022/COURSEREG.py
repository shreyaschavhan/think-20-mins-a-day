# cook your dish here

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    if (m >= (n+k)):
        print("Yes")
    else:
        print("No")
