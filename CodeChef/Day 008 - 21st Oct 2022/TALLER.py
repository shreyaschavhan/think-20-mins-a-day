# cook your dish here

for _ in range(int(input())):
    A, B = [int(x) for x in input().split()]
    if A > B:
        print('A')
    else:
        print('B')
