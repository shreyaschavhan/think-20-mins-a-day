# cook your dish here

for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    freq = {}
    flag = 1
    for i in A:
        if i in freq:
            freq[i] += 1
            if freq[i] > 2:
                flag = 0
                break
        else:
            freq[i] = 1

    if flag:
        print('Yes')
    else:
        print('No')
    
