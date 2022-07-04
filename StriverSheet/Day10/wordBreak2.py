class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtrack(i, stack):
            if i == len(s):
                res.append(stack[:-1])
                return
            for j in range(i, len(s)+1):
                if s[i:j] in wordDict:
                    backtrack(j, stack+s[i:j]+" ")

        backtrack(0, "")
        return res
