# https://atcoder.jp/contests/abc137/tasks/abc137_c

import math

import sys
import collections

n=int(input())
a=[''.join(sorted(input())) for _ in range(n)]

ans = 0
for v in collections.Counter(a).values():
    for i in range(1, v):
        ans += i
print(ans)