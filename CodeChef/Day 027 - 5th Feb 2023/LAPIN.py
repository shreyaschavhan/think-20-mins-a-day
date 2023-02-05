# cook your dish here

for _ in range(int(input())):
    word = input()
    length = len(word)//2
    if sorted(word[:length]) == sorted(word[-length:]):
        print("YES")
    else:
        print("NO")
