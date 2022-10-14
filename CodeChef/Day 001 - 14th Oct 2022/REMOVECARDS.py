# https://www.codechef.com/submit/REMOVECARDS

t = int(input())

for i in range(t):
    n = int(input())
    freq = {}
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] in freq.keys():
            freq[a[j]] += 1
        else:
            freq[a[j]] = 1
    s = sorted(freq.values())
    if len(s) == 1:
        print("0")
    else:
        min_sum = 0
        for k in range(len(s)-1):
            min_sum += int(s[k])
        print(min_sum)
