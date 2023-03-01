# cook your dish here
# https://www.codechef.com/LP2TO301/problems/INDIPERM

for _ in range(int(input())):
    N = int(input())
    answer = []
    if N % 2 == 0:
        answer.append(N)
        for i in range(1, N):
            answer.append(i)
    else:
        for i in range(2, N+1):
            answer.append(i)
        answer.append(1)
    
    print(*answer)
                