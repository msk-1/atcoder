# https://atcoder.jp/contests/abc139/tasks/abc139_b

l = [input() for i in range(1)]
nums = [int(i) for i in l[0].split(' ')]
tap = nums[0]
want = nums[1]
plug = 1
num = 0
while plug < want:
    plug -= 1
    plug += tap
    num += 1
print(num)