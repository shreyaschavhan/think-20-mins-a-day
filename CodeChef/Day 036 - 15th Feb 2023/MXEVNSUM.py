# cook your dish here
# https://www.codechef.com/LP1TO201/problems/MXEVNSUB

for _ in range(int(input())):
    N = int(input())

    if (N * (N + 1) / 2) % 2 == 0:
        print(N)
    else:
        print(N-1)
