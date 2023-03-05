# cook your dish here
# https://www.codechef.com/LP2TO301/problems/MINPIZZAS

import math

for _ in range(int(input())):
    N, K = map(int, input().split())
    print(math.lcm(N, K) // K)
