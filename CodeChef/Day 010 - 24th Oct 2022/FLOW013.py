# https://www.codechef.com/LP0TO101/problems/FLOW013

# cook your dish here

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b + c == 180:
        print("YES")
    else:
        print("NO")
