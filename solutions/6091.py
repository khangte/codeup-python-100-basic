# CodeUp Problem 6091.py

a, b, c= map(int, input().split())
d=1
while 1:
    if d%a==0 and d%b==0 and d%c==0:
        break
    d+=1
print(d)
