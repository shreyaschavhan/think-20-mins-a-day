# cook your dish here

for _ in range(int(input())):
    N = int(input())
    H = list(map(int, input().split()))
    maxocc = max(H, key=H.count)
    maxcount = H.count(maxocc)
    maxH = 0 
    for i in range(maxcount):
        maxH += maxocc
        maxocc += 1 
        
    print(maxH)