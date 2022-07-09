class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            cursum = 0
            count = 1  # atleast one subarray

            for i in nums:
                cursum += i
                if cursum > largest:
                    count += 1
                    cursum = i
            return count <= m

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = l + ((r-l)//2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
