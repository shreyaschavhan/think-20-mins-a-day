from functools import reduce

for _ in range(int(input())):
    N = int(input())
    sequence = [i for i in range(1, N+1)]
    length = 1
    for i in range(N):
        for j in range(i+1, N+1):
          if reduce(lambda x, y: x & y, sequence[i:j]) > 0:
            length = max(length, len(sequence[i:j]))

    print(length)
