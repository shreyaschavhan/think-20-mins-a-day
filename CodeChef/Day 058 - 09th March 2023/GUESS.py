# cook your dish here
# https://www.codechef.com/LP2TO308/problems/GUESS

from fractions import Fraction

def reduce_fraction(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    return fraction.numerator, fraction.denominator

for _ in range(int(input())):
    N, M = map(int, input().split())
    total = N * M 
    alice = total // 2

    reduced_num, reduced_denom = reduce_fraction(alice, total)
    print(f'{reduced_num}/{reduced_denom}')