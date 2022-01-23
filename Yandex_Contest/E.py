import sys
from typing import Counter

line_1 = sys.stdin.readline().strip()
line_2 = sys.stdin.readline().strip()

dict_1 = Counter[line_1]
dict_2 = Counter[line_2]

if dict_1 == dict_2:
    print(1)
else:
    print(0)
