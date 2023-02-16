# https://www.codechef.com/LP1TO201/problems/MANYSUMS
# cook your dish here

for _ in range(int(input())):
    l, r = map(int, input().split())
    print((r+r)-(l+l)+1)
