# CodeUp Problem 6090.py

a, m, d, n = map(int, input().split())
result=a
for i in range(2, n+1):
    result=result*m+d
print(result)
