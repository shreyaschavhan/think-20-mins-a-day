# cook your dish here

for _ in range(int(input())):
    N = int(input())
    if N == 2:
        print(N)
    else:
        while N > 0:
            if (N * (N + 1) / 2) % 2 == 0:
                print(N)
                break
            N -= 1
