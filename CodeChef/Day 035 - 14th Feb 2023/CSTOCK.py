# https://www.codechef.com/LP1TO201/problems/CSTOCK
# cook your dish here

for _ in range(int(input())):
    s, a, b, c = map(int, input().split())
    price = (s + (c*s/100))
    if  price >= a and price <= b:
        print('yes')
    else:
        print('no')
