class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max1 = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max1 = max(max1, count)
        return max1
