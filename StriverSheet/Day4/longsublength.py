class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        res = 0
        visited = set()

        # sliding window approach
        while start < len(s) and end < len(s):
            if s[end] not in visited:
                visited.add(s[end])
                end += 1
                res = max(res, end - start)
            else:
                visited.remove(s[start])
                start += 1
        return res
