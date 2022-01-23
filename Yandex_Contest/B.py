import sys

n = sys.stdin.readline().strip()
array = []
for i in range(0, int(n)):
    array.append(int(sys.stdin.readline().strip()))

cur, best = 0, 0
for i in array:
    if i == 1:
        cur += 1
        best = max(best, cur)
    else:
        cur = 0
print(max(best, cur))
