# Intuit 2022
def minSwaps(nums):
    count,temp = 0,0
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 0:
            temp+= 1
        else:
            count += temp
    return count

print(minSwaps([0,0,1,0,1,0,1,1]))