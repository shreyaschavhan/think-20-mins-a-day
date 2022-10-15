# https://www.codechef.com/submit/FLIPPAL
# wrong answer - do it again tomorrow

t = int(input())

for _ in range(t):

    frequency = {'0': 0, '1': 0}
    n = int(input())
    binary_string = input()
    for i in range(n):
        frequency[binary_string[i]] += 1

    if n == 1:
        print('YES')
        continue

    if n % 2 != 0:
        if frequency['0'] % 2 == 0 or frequency['1'] % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if frequency['0'] % 2 == 0 and frequency['1'] % 2 == 0:
            print("YES")
        elif frequency['0'] % 2 != 0 and frequency['1'] % 2 != 0:
            if n == 2:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
