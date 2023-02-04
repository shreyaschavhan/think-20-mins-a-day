# https://www.codechef.com/CCSTART2/problems/ANGTRICH?tab=statement
# cook your dish here

angles = [int(x) for x in input().split()]
if sum(angles) == 180 and (0 not in angles):
    print("YES")
else:
    print("NO")
