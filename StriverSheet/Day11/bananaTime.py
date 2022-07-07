class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r-l)//2
            total = 0
            for i in piles:
                total += ((i-1)//m)+1

            if total <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
