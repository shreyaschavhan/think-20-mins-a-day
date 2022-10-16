# cook your dish here

t = int(input())
for _ in range(t):
    n, k = input().split()
    if int(n) < int(k):
        print("YES")
    else:
        print("NO")
