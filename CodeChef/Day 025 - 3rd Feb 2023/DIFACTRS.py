# cook your dish here

N = int(input())
factors = []

for i in range(1, N+1):
    if N % i == 0:
        factors.append(i)

print(len(factors), *factors)
