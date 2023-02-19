# cook your dish here
# https://www.codechef.com/LP1TO205/problems/SIMPSTAT

for _ in range(int(input())):
    N, K = map(int, input().split())
    A = sorted(list(int(x) for x in input().split()))
    if K != 0:
        newarray = A[K:-K]
        print(f'{sum(newarray)/len(newarray):.6f}')
    else:
        print(f'{sum(A)/N:.6f}')