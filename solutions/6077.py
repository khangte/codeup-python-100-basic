# CodeUp Problem 6077.py

n = int(input())
sum=int(0)
for i in range(1, n+1):
    if(i%2==0): sum+=i
print(sum)
