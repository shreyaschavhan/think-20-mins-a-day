# cook your dish here

directions = ["North", "East", "South", "West"]

for _ in range(int(input())):
    x = int(input())
    print(directions[x % 4])
    
