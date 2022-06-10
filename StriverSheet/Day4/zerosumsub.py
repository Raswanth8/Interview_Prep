# Largest Subarray with 0 sum
def zerosubarr(nums):
    hMap = {}
    hMap[0] = 0
    length = -1
    cursum = 0

    for i in range(len(nums)-1):
        cursum = cursum + nums[i]
        if cursum in hMap:
            length = max(length, i+1-length)
        else:
            length = i+1-length
    return length


print(zerosubarr([15, -2, 2, -8, 1, 7, 10, 23]))
