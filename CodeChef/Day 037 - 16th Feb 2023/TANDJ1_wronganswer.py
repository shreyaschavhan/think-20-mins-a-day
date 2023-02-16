# https://www.codechef.com/LP1TO201/problems/TANDJ1
# cook your dish here

for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    difference = abs((c+d) - (a+b))
    if k == difference:
        print('YES')
    elif k > difference:
        if (not(difference % 2) and not(k % 2)) or ((difference % 2) and (k % 2)):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
            
