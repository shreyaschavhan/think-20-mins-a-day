# cook your dish here
# https://www.codechef.com/LP2TO301/problems/MANYSUMS

for _ in range(int(input())):
    l, r = map(int, input().split())
    print((r+r)-(l+l)+1)