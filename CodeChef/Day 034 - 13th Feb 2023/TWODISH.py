# https://www.codechef.com/LP1TO201/problems/TWODISH
# cook your dish here

for _ in range(int(input())):
    N, fruits, vegetables, fishes = map(int, input().split())
    if N <= vegetables and  (fruits+fishes) >= N:
        print('YES')
    else:
        print('NO')
