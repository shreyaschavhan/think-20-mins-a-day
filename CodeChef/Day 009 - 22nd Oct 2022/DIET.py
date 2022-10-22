# cook your dish here

for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    required = n * k
    count = 0
    total = 0
    a = [int(x) for x in input().split()]
    stored = 0
    for i in range(n):
        if a[i] >= k:
            stored += a[i] - k
        else:
            if (a[i] + stored) >= k:
                stored = ((stored + a[i]) - k)
            else:
                count = i + 1
                break
        total += a[i]

    if required <= total:
        print("YES")
    else:
        print("NO", count)
        
