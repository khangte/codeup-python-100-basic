# CodeUp Problem 6084.py

h, b, c, s=map(int, input().split())
store=format(h*b*c*s/8/1024/1024, '.1f')
print(store, 'MB')
