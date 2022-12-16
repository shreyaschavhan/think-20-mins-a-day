for _ in range(int(input())):
    length = input()
    s = int(input(), 2)
    result = [s ^ int(s / (2 ** y)) for y in range(10)]
    print(result.index(max(result)))


    
