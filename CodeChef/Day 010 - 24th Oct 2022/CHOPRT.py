# https://www.codechef.com/LP0TO101/problems/CHOPRT

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")
