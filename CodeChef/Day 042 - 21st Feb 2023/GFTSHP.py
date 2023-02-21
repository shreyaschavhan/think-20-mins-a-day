# cook your dish here
# https://www.codechef.com/LP1TO205/problems/GFTSHP
import math

for _ in range(int(input())):
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    count = 0
    sum = 0
    for i in range(len(A)):
        discounted = math.ceil(A[i] / 2)
        if (sum + discounted) <= K:
            sum += A[i]
            count += 1 
        else:
            break 
            
    print(count)
            
            
        
    