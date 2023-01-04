
for _ in range(int(input())):
    following, follower = map(int, input().split())
    if following > 10 * follower:
        print("YES")
    else:
        print("NO")
