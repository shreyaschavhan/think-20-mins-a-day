# cook your dish here

from fractions import Fraction

def reduce_fraction(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    return fraction.numerator, fraction.denominator

for _ in range(int(input())):
    N, M = map(int, input().split())
    alice = 0
    total = 0
    for i in range(1, N+1):
        min_sum = i + 1
        max_sum = i + M 
        if (max_sum - min_sum) == 0:
            if max_sum % 2:
                alice += 1
        else:
            for i in range(min_sum, max_sum+1):
                if i % 2:
                    alice += 1
        total += (max_sum + 1 - min_sum)
    reduced_num, reduced_denom = reduce_fraction(alice, total)
    print(f'{reduced_num}/{reduced_denom}')