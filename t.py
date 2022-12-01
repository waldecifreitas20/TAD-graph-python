from collections import deque

d = deque([0])
d.append(0)
l = [12,21]
d.extend(l)
print(d)