# CodeUp Problem 6096.py

x, y = 19, 19
d = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    input_number = list(map(int, input().split()))
    for j in range(y):
        d[i][j]= input_number[j]

n=int(input())
for i in range(n):
    a,b = input().split()
    a = int(a)-1; b= int(b)-1
    for j in range(x):
        if d[a][j]==0: d[a][j] =1
        else: d[a][j] =0

        if d[j][b]==0: d[j][b]=1
        else: d[j][b]=0

for i in range(x):
    for j in range(y):
        print(d[i][j], end=" ")
    print()
