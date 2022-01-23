import sys

count = sys.stdin.readline().strip()

ch = -1
res = []
for i in range(int(count)):
    el = sys.stdin.readline().strip()
    if el != ch:
        res.append(el)
    ch = el

for i in res:
    print(i)
