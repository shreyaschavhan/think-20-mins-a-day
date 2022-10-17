# https://www.codechef.com/submit/EZSPEAK

vowels = ['a', 'e', 'i', 'o', 'u']

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = 1
    for i in range(1, n):
        if s[i] not in vowels:
            if s[i-1] not in vowels:
                count += 1
            else:
                count = 1
        if count == 4:
            print("NO")
            break

    if count < 4:
        print("YES")
