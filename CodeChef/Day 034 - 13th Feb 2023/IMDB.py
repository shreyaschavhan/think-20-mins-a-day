# cook your dish here

for _ in range(int(input())):
    N, X = map(int, input().split())
    rating = 0
    for __ in range(N):
        S, R = map(int, input().split())
        if S <= X:
            rating = max(rating, R)
    print(rating)
