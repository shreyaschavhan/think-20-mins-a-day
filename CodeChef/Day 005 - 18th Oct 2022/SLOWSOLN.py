# SLOWSOLN


for _ in range(int(input())):
    maxT, maxN, sumN = [int(x) for x in input().split()]
    T = 0
    N = 0
    output = 0
    while sumN > 0 and T < maxT:
        if maxN < sumN:
            N = maxN
        else:
            N = sumN
        output += N * N
        sumN -= N
        T += 1
    print(output)
