# https://atcoder.jp/contests/abc139/tasks/abc139_a

l = [input() for i in range(2)]

count = 0
ex = l[0]
ac = l[1]

for i in range(3):
    if ex[i] == ac[i]:
        count = count + 1
print(count)