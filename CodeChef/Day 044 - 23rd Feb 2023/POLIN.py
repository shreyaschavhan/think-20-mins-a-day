# cook your dish here
# https://www.codechef.com/LP1TO205/problems/POLIN

for _ in range(int(input())):
    N = int(input())
    answer_x = set()
    answer_y = set()
    for __ in range(N):
        x, y = map(int, input().split())
        answer_x.add(x)
        answer_y.add(y)
    print(len(answer_x) + len(answer_y))