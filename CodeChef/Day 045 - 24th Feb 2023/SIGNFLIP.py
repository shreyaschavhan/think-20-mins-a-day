# cook your dish here
# https://www.codechef.com/LP1TO205/problems/SIGNFLIP

for _ in range(int(input())):
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    sum = 0
    for i in A:
        if i < 0 and K > 0:
            sum += (-1 * i)
            K -= 1 
        elif i > 0:
            sum += i 
    print(sum)
    
    
            
            
        