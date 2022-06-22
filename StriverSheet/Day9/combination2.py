class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(pos, combination, target):
            if target == 0:
                res.append(combination[::])
            if target <= 0:
                return

            prev = -1

            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                combination.append(candidates[i])
                backtrack(i+1, combination, target-candidates[i])
                combination.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res
