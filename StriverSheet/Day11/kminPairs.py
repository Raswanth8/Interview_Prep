class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        l, r = 0, max(nums) - min(nums)
        while l < r:
            m = l + (r-l) // 2
            if self.enough(nums, k, m):
                r = m
            else:
                l = m + 1
        return l

    def enough(self, nums, k, diff):
        slow, fast, count = 0, 1, 0

        while slow < len(nums) or fast <= len(nums)-1:
            while fast <= len(nums)-1 and nums[fast] - nums[slow] <= diff:
                fast += 1
            count += fast - slow - 1
            slow += 1
        return count >= k
