def count_inv(nums):
    count_inv = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if(nums[i] > nums[j]):
                count_inv += 1
    return count_inv


print(count_inv([3, 2, 1]))
