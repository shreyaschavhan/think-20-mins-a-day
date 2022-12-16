for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [int(_) for _ in input().split()]

    if sum(a) == n:
        print(100)
    elif sum(a[:m]) == m:
        print(k)

    else:
        print(0)
