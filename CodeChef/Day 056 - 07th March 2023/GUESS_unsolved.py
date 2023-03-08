
for _ in range(int(input())):
    N, M = map(int, input().split())
    alice, bob = 0, 0
    for i in range(1, N+1):
        min_sum = i + 1
        max_sum = i + M 
        if (max_sum - min_sum) == 0:
            if max_sum % 2 == 0:
                bob += 1
            else:
                alice += 1 
        else:
            temp_max = max_sum
            temp_min = min_sum
            if max_sum % 2:
                temp_max = max_sum + 1
            if min_sum % 2:
                temp_min = min_sum - 1 
            bob += (temp_max - temp_min) // 2
            alice += ((max_sum-min_sum) - (temp_max - temp_min) // 2)
        print(alice, bob)