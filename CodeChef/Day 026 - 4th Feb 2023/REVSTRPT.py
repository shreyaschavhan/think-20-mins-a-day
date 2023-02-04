# https://www.codechef.com/CCSTART2/problems/REVSTRPT
# cook your dish here
N = int(input())
space = ' '
for stars in range(1, N+1):
    print(f"{space * (N - stars)}" + '*' * stars)
