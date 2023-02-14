# https://www.codechef.com/LP1TO201/problems/WEIGHTBL
# cook your dish here

for _ in range(int(input())):
    w1, w2, x1, x2, M = map(int, input().split())
    change = w2 - w1
    mini, maxi = (x1 * M), (x2 * M)
    if change < mini or change > maxi:
        print(0)
    else:
        print(1)
