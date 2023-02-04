# https://www.codechef.com/CCSTART2/problems/EXTRICHK

a, b, c = map(int,input().split())
if (a + b) > c and (a + c) > b and (b + c) > a :
    if a == b and b == c:
        print(1)
    elif a == b or b ==c or a == c:
        print(2)
    else:
        print(3)
else:
    print(-1)
