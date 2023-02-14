# https://www.codechef.com/LP1TO201/problems/PROBCAT

for _ in range(int(input())):
    x = int(input())
    if 1 <= x and x < 100:
        print('Easy')
    elif 100 <=x and x < 200:
        print('Medium')
    else:
        print('Hard')
