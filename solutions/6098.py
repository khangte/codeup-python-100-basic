# CodeUp Problem 6098.py

h, w = 10, 10
board = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    input_number = list(map(int, input().split()))
    for j in range(w):
        board[i][j]= input_number[j]

ant_location_x,ant_location_y = 1,1

while True:
    if board[ant_location_x][ant_location_y] == 0:
        board[ant_location_x][ant_location_y] = 9
    elif board[ant_location_x][ant_location_y] == 2:
        board[ant_location_x][ant_location_y] = 9
        break

    if board[ant_location_x][ant_location_y + 1] == 1:
        if board[ant_location_x + 1][ant_location_y] == 1:
            board[ant_location_x][ant_location_y] = 9
            break
        else: ant_location_x += 1
    else: ant_location_y += 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=" ")
    print()
