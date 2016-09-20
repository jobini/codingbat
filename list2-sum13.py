def sum13(nums):
    if nums == []:
        return 0
    else:
        sum = 0
        i = 0
        while i <= len(nums)-1:
            if nums[i] == 13:
                if i == len(nums) - 1:
                    return sum
                else:
                    if nums[i+1] == 13:
                        i += 1
                        continue
                    else:
                        i += 2
            else:
                sum += nums[i]
                i += 1
        return sum
