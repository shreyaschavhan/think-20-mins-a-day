# cook your dish here
# https://www.codechef.com/LP1TO205/problems/EVENSPLIT

for _ in range(int(input())):
    N = int(input())
    S = input()
    if N <= 2:
        print(S)
    else:
        print(''.join(sorted(S)))
