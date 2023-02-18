# cook your dish here
# https://www.codechef.com/LP1TO205/problems/HOLIDAYS

for _ in range(int(input())):
    n, w = map(int, input().split())
    A = [int(__) for __ in input().split()]
    count = 0
    for i in sorted(A, reverse=True):
        if w <= 0:
            count += 1
        else:
            w -= i 
    print(count)
        