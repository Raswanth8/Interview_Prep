class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        rarr = []

        def search(target):
            l, h = 0, len(rarr)
            while l < h:
                mid = (l+h) // 2
                if target <= rarr[mid]:
                    h = mid
                else:
                    l = mid + 1
            return l

        for i in range(len(nums)-1, -1, -1):
            ans += search(nums[i]/2)
            rarr.insert(search(nums[i]), nums[i])
        return ans
