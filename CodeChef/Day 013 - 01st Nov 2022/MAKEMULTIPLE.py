# cook your dish here

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:                  # Base Case I think?
        print("YES")
    elif (b/2) >= a:
        # For any number to be multiple of some number, it's necessary for it to be either equal or greater than twice the number to divide it with. It's impossible otherwise because you wanna add a common number to both the terms a and b.
        print("YES")
    else:
        print("NO")
