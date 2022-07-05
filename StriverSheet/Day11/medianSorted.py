class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        total = len(nums1) + len(nums2)
        half = total//2

        if len(nums1) > len(nums2):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            i = (l+r) // 2  # A
            j = half - i - 2  # B , j is a index

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if j+1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r -= 1
            else:
                l += 1
