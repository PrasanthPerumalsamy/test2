def find_sum_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return None

output = find_sum_pair([4,2,6,2,5], 4)
print(output)