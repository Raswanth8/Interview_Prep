def countPairs(nums, target):
    pMap = {}
    count = 0

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in pMap:
            count += pMap[diff]
        if nums[i] in pMap:
            pMap[nums[i]] += 1
        else:
            pMap[nums[i]] = 1
    return count


print(countPairs([1, 5, 7, -1, 5], 6))

# Amazon Interview
