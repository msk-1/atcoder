# https://atcoder.jp/contests/abc137/tasks/abc137_b

l = [int(i) for i in input().split(' ') for l in range(1)]
for i in range((l[1] - l[0] + 1), (l[1] + l[0])):
    print(i)