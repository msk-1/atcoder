# import sys
 
# n=int(input())
# a=[input() for i in range(n)]
 
# num = 0
# sortedA = []
 
# https://atcoder.jp/contests/abc137/tasks/abc137_c

import sys
import collections

n=int(input())
a=[''.join(sorted(input())) for _ in range(n)]

ans = 0
for v in collections.Counter(a).values():
    if v != 1:
        ans += v * (v - 1) // 2
print(ans)