# https://atcoder.jp/contests/abc138/tasks/abc138_c

input_list = [input() for i in range(2)]

maxNum = int(input_list[0])

nums = [int(i) for i in input_list[1].split(' ')]

nums.sort()

value = 0
is_first_item = True
index = maxNum - 1
for num in nums:
    if is_first_item:
        value = value + num / (2 ** index)
        is_first_item = False
    else:
        value = value + num / (2 ** index)
        index = index - 1

print(value)

