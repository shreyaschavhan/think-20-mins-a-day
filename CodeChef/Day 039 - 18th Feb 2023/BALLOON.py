# cook your dish here
# https://www.codechef.com/LP1TO205/problems/BALLOON

for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    problems = [x for x in range(1, 8)]
    sum = 28
    count = 0
    for i in A:
        if i in problems:
            sum -= i 
        count += 1
        if sum == 0:
            break
    print(count)