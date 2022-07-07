class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while(l < r):
            if nums[l] <= nums[r]:
                res = min(nums[l], res)
                break
            mid = l + (r-l)//2
            if nums[l] < nums[mid]:
                res = min(nums[mid], nums[l])
                l += 1
            else:
                res = min(nums[mid], nums[r])
                r -= 1
        return res
