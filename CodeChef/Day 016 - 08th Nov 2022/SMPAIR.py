# cook your dish here

for _ in range(int(input())):
    N = int(input())
    a = [int(x) for x in input().split()]
    if (N <= 2):
        print(a[0] + a[1])
    else:
        a.sort()
        print(a[0] + a[1])
