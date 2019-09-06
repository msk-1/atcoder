# https://atcoder.jp/contests/abc138/tasks/abc138_b

import sys
lst = []
for line in sys.stdin:
    if line == '\n':
        break
    else :
        lst.append(line)

n = int(lst[0])
intList = lst[1].split(' ')
mother = 0
for item in intList:
    mother = mother + (1/int(item))
print(1/mother)