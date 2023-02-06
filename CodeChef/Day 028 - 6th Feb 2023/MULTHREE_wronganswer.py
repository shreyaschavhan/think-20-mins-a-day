# cook your dish here

for _ in range(int(input())):
    K, d0, d1 = map(int, input().split())
    sum = (d0 + d1) % 10
    print(f'{d0}{d1}', end='')
    length = 2
    for i in range(K-2):
        print(sum%10, end='')
        if sum % 10 == 0:
            # print("\nlength:", length)
            break
        if sum % 10 == 2:
            # print("\nlength:", length)
            break
        sum += sum % 10
        length += 1
    print()
    remaining = (K-length)
    if length == 2 or length == 3:
        pass
    else:
        sum += 20 * (remaining // 4)
        if remaining % 4 == 1:
            sum += 2
        elif remaining % 4 == 2:
            sum += 6
        elif remaining % 4 == 3:
            sum += 14
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
