# cook your dish here
# https://www.codechef.com/LP2TO308/problems/FILL01

for _ in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    string_K = '0' * K 
    nap = 0
    i = 0
    while i < N:
        temp_S = S[i: i + K]
        if '1' in temp_S:
            i += temp_S.index('1') + 1 
        if temp_S == string_K:
            nap += 1
            i += K
    print(nap)