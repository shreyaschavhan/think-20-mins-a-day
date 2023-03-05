
# cook your dish here
# https://www.codechef.com/LP2TO301/problems/NFS

import math

for _ in range(int(input())):
    u, v, a, s = map(int, input().split())
    u_2 = u ** 2 
    _2as = 2 * a * s 
    if v ** 2 >= (u_2 - _2as):
        print('yes')
    else:
        print('no')