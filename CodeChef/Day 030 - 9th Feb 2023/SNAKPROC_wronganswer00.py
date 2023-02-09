# cook your dish here

for _ in range(int(input())):
    __ = int(input())
    report = input().replace('.', '').strip()
    if len(report) % 2 == 0:
        if 'HH' in report or 'LL' in report:
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')

    
