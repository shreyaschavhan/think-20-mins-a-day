# https://www.codechef.com/LP1TO201/problems/NFS
# cook your dish here
import math

for _ in range(int(input())):
    u, v, a, s = map(int, input().split())
    u_2 = u ** 2
    _2as = 2 * a * s
    if v ** 2 >= (u_2 - _2as):
        print('yes')
    else:
        print('no')
