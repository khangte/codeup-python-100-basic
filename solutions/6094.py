# CodeUp Problem 6094.py

n = int(input())
k = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if k[i]> k[j]:
            temp = k[i]
            k[i] = k[j]
            k[j] = temp
print(k[0])
