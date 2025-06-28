def pipe_fix(nums):
    first_item = nums[0]
    last_item = nums[-1]
    return list(range(first_item, last_item + 1))


print(pipe_fix([1, 2, 3, 12]))
