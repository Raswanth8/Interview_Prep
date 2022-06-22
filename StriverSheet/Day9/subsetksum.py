class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)/k
        used = [False]*len(nums)

        def backtrack(i, k, total):
            if k == 0:
                return True
            if total == target:
                return backtrack(0, k-1, 0)

            for j in range(i, len(nums)):
                if used[j] or total + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1, k, total+nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0, k, 0)
