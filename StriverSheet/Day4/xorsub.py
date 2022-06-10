class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        import collections
        hashT = collections.defaultdict(bool)
        hashT[0] = 1
        cursum = 0
        count = 0

        for i in A:
            cursum ^= i
            if hashT[cursum ^ B]:
                count += hashT[cursum ^ B]
            hashT[cursum] += 1
        return count
