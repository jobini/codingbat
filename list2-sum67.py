def sum67(nums):
    if nums == []:
        return 0
    i = 0
    sum = 0
    while i <= len(nums) - 1:
        if nums[i] == 6:
            if i == len(nums) - 1:
                return sum
            else:
                while nums[i] != 7:
                    i += 1
                if i == len(nums) - 1:
                    return sum
                else:
                    i += 1
                    continue
        else:
            sum += nums[i]
            i += 1
    return sum
