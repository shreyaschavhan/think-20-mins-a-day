
# cook your dish here
# https://www.codechef.com/LP1TO205/problems/COOKMACH

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A == B:
        print(0)
    else:
        answer = 0
        while (B % A) != 0:
            A = A // 2 
            answer += 1 
        while B != A:
            A *= 2
            answer += 1 
        print(answer)
