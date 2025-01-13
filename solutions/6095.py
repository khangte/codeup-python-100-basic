# CodeUp Problem 6095.py

n = int(input())
x, y = 20, 20
checkboard = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    for j in range(y):
        checkboard[i][j]=0

for i in range(n):
    kx, ky = map(int, input().split())
    checkboard[kx][ky]=1

for i in range(1, x):
    for j in range(1, y):
        print(checkboard[i][j], end=" ")
    print()
