# https://www.codechef.com/CCSTART2/problems/SQALPAT

N = int(input())

initial = 1
for line in range(1, N+1):
    if line % 2:
        print(*list(range(initial, (line * 5) + 1)))
    else:
        print(*reversed(list(range(initial, (line * 5) + 1))))
    initial = (line*5)+1
