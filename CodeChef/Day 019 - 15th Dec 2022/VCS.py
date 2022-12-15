for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = {int(x) for x in input().split()}
    b = {int(x) for x in input().split()}
    all = set(range(1, n+1))
    print(len(a.intersection(b)), len((all.difference(a)).intersection(all.difference(b))))

    
