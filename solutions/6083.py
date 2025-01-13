# CodeUp Problem 6083.py

r,g,n= map(int,input().split())
count=0
for i in range(0,r):
    for j in range(0,g):
        for k in range(0,n):
            print(i, j, k)
            count+=1
print(count)
