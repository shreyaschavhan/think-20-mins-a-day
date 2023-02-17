# cook your dish here
# https://www.codechef.com/LP1TO205/problems/MATCHES

matches = {'0':6,'1':2,'2':5,'3':5,'4':4, '5':5, '6':6, '7':3, '8':7,'9': 6}
for _ in range(int(input())):
    a, b = map(int, input().split())
    sum = str(a+b)
    count = 0
    for i in sum:
        count += matches[i]
    print(count)