class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        res = []
        n = len(A)
        S = (n*(n+1))/2
        P = (n*(n+1)*(2*n+1))/6

        for i in range(n):
            S -= A[i]
            P -= A[i]*A[i]

        missing = (S+P/S)/2
        repeating = missing - S

        return repeating, missing
