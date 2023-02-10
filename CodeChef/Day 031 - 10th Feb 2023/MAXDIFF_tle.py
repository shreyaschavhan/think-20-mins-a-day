# https://www.codechef.com/LP1TO201/problems/MAX_DIFF

from itertools import combinations


for _ in range(int(input())):
    n, s = map(int, input().split())

    max_diff = 0
    for comb in combinations(range(n+1), 2):
        if sum(comb) == s:
            max_diff = max(abs(comb[0] - comb[1]), max_diff)
    print(max_diff)
