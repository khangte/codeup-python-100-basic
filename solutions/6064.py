# CodeUp Problem 6064.py

a,b,c = input().split()
a,b,c = int(a),int(b), int(c)
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(d)
