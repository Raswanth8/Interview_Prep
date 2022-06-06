class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        h = {}
        res = []

        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        for key, value in h.items():
            if value > len(nums)//3:
                res.append(key)
        return res
