def can_move(current_color, next_color):
    if current_color == next_color:
        return 0
    else:
        return 1

for _ in range(int(input())):
    a, b, p, q = map(int, input().split())
    moves = 0
    if (a, b) == (p, q):
        pass
    else:
        current_color = (a + b) % 2
        next_color = (p + q) % 2
        if can_move(current_color, next_color):
            moves += 1
        else:
            moves += 2
    print(moves)


        
