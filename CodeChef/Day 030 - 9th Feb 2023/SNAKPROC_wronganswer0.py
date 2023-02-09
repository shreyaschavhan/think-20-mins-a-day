# cook your dish here

for _ in range(int(input())):
    __ = int(input())
    report = input().replace('.', '').strip()
    valid = 1
    check = ''
    if len(report) == 0:
        print('Valid')
    elif len(report) % 2 != 0:
        print('Invalid')
    else:
        check = report[0]
        for i in range(1, len(report)):
            if check == report[i]:
                valid = 0
            else:
                check = report[i]

        if valid:
            print('Valid')
        else:
            print('Invalid')
