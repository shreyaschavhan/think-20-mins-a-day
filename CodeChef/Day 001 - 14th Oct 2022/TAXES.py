# https://www.codechef.com/submit/TAXES

t = int(input())
for i in range(t):
    x = int(input())
    if x > 100:
        print(x - 10)
    else:
        print(x)
