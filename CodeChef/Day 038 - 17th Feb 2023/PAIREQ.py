# cook your dish here
# https://www.codechef.com/LP1TO205/problems/PAIREQ

for _ in range(int(input())):
    N = int(input())
    A = sorted(input().split())
    print(N-A.count(max(A, key=A.count)))
    