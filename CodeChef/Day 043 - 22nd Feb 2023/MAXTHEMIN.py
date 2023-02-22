# cook your dish here
# https://www.codechef.com/LP1TO205/problems/MAXTHEMIN

for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K >= len(A):
        print(max(A))
    else:
        print(sorted(A)[K])