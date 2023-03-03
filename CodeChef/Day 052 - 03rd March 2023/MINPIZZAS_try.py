# cook your dish here

def solution(N, K):
    if N == 1:
        return 1
    if K == 1:
        return N
    solution_set = set()
    for i in range(1, N+1):
        if N % i == 0:
            solution_set.add(i)
    
    for i in solution_set:
        if N % i == 0 and K % i == 0:
            return i


for _ in range(int(input())):
    N, K = map(int, input().split())
    print(solution(N, K))
        
        
    
        