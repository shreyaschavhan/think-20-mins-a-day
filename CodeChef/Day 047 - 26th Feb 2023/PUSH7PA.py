# cook your dish here
# https://www.codechef.com/LP1TO205/problems/PUSH7PA

for _ in range(int(input())):
    N = int(input())
    H = list(map(int, input().split()))
    uniqueH = set(H)
    maxH = 0
    for i in uniqueH:
        maxH = max(maxH, i + H.count(i) - 1)
    print(maxH)