def centered_average(nums):
    sum = 0
    for i in nums:
        sum = sum + i
    sum = sum - (max(nums) + min(nums))
    mean = sum/(len(nums) - 2)
    return mean
