class Solution:
    # @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        low, high = max(A), sum(A)
        if B == 1:
            return low
        elif B < 1 or B > len(A):
            return -1
        while low < high:
            mid = (low + high)//2
            count = self.isPossible(A, mid)
            if count > B:
                low = mid + 1
            else:
                high = mid
        return low


    def isPossible(self,A,mid):
        total = 0
        count = 1
        
        for i in A:
            if total+i <= mid:
                total += i
            else:
                count += 1
                total = i
        return count