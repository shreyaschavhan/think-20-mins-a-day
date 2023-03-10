# cook your dish here
# https://www.codechef.com/LP2TO308/problems/POLYREL

for _ in range(int(input())):
    N = int(input())
    for __ in range(N):
        _xy_ = input()
    
    
    answer = 0
    while N > 0:
        if N > 2:
            answer += N
        else:
            break 
        N = N // 2
    print(answer)