# cook your dish here
# https://www.codechef.com/LP1TO205/problems/GFTSHP

for _ in range(int(input())):
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    count = 0
    for i in range(len(A)):
        if (K - A[i]) == 0:
            count += 1
            break
        elif (K - A[i]) > 0:
            K -= A[i]
            count += 1
        else:
            # i -= 1
            # K += A[i]
            if (K - A[i] // 2) >= 0:
                count += 1


    print(count)
