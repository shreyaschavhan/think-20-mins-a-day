# https://www.codechef.com/LP1TO201/problems/CHFSPL
# cook your dish here

for _ in range(int(input())):
    A, B, C = map(int, input().split())
    print(max(A+B, B+C, A+C))
