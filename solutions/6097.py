# CodeUp Problem 6097.py

h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        board[i][j]= 0

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    x-=1; y-=1

    if d==0:
        for j in range(l):
            board[x][y+j]=1
    elif d==1:
        for j in range(l):
            board[x+j][y]=1

for i in range(h):
    for j in range(w):
        print(board[i][j], end = ' ')
    print()
