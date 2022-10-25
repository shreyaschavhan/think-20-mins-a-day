# https://www.codechef.com/LP1TO201/problems/VDATES

for _ in range(int(input())):
    d, l, r = map(int, input().split())

    if l <= d <= r:
        print("Take second dose now")
    else:
        if d < l:
            print("Too Early")
        else:
            print("Too Late")
