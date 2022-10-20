# cook your dish here

for _ in range(int(input())):
    n = int(input())
    s = input()
    operations = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            operations += 1
    print(operations)
