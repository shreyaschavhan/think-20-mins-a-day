# cook your dish here

for _ in range(int(input())):
    rangee = ""
    for i in range(int(input())):
        rangee += '9'
    starting = rangee[:-1]
    if starting == "":
        starting = 0
    for i in range(int(starting), int(rangee)):
        if i % 3 == 0 and i % 9 != 0 and i % 2 !=0:
            print(i)
            break


                
