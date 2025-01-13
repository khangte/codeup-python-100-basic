# CodeUp Problem 6085.py

w, h, b = map(int, input().split())
store = format(w*h*b/8/1024/1024, '.2f')
print(store, 'MB')
