# https://atcoder.jp/contests/abc136/tasks/abc136_b

a = [int(input()) for i in range(1)][0]
r = 0

for i in reversed(range(0, a)):
    if (len(str(a)) % 2) != 0:
        r = r + 1
    a = a - 1
print(r)