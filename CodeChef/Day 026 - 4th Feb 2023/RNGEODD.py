# https://www.codechef.com/CCSTART2/problems/RNGEODD# cook your dish here

L, R = map(int, input().split())
for i in range(L, R+1):
    if i % 2:
        print(i, end=' ')
