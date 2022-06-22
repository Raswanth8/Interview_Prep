class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i,combination,total):
            if total == target:
                res.append(combination[:])
                return
            
            if i >= len(candidates) and total > target:
                return
            
            combination.append(candidates[i])
            backtrack(i,combination,total+candidates[i])
            combination.pop()
            
            backtrack(i+1,combination,total)
        
        backtrack(0,[],0)
        return res