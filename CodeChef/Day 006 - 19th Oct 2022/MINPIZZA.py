# MINPIZZA

for _ in range(int(input())):
    n, x = [int(x) for x in input().split()]
    max_required = n * x
    pizza = 0
    while True:
        if pizza * 4 < max_required:
            pizza += 1
        else:
            break
    print(pizza)
