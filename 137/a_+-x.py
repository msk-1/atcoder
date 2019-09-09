# https://atcoder.jp/contests/abc137/tasks/abc137_a

i = [int(i) for i in input().split(' ') for l in range(1)]

print(max(i[0] + i[1], i[0] - i[1], i[0] * i[1]))