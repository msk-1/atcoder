# https://atcoder.jp/contests/abc136/tasks/abc136_a

a = [int(i) for i in input().split()] 
r = a[2] - (a[0] - a[1])
l = lambda r: print(r) if r > 0 else print(0)
l(r)