# https://www.codechef.com/submit/ATM2

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    withdraw = [int(x) for x in input().split()]
    for i in withdraw:
        if i <= k:
            print(1, end='')
            k -= i
        else:
            print(0, end='')
    print()
