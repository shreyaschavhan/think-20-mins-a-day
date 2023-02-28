# cook your dish here
# https://www.codechef.com/LP2TO301/problems/MAKEDIV3

for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(3)
    elif N == 2:
        print(15)
    elif N == 3:
        print(123)
    else:
        print('1' + '0' * (N - 2) + '5')
             
                