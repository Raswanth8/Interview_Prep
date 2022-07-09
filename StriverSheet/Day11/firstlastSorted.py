class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binsearch(nums, target, True)
        right = self.binsearch(nums, target, False)

        return [left, right]

    def binsearch(self, nums, target, leftbias):
        l, r = 0, len(nums)-1
        i = -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
            else:
                i = mid
                if leftbias:
                    r -= 1
                else:
                    l += 1
        return i
