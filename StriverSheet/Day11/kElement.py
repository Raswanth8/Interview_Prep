# User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i = 0
        j = 0
        d = 0
        res = [0] * (m+n)

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                res[d] = arr1[i]
                i += 1
            else:
                res[d] = arr2[j]
                j += 1
            d += 1
        while i < n:
            res[d] = arr1[i]
            d += 1
            i += 1
        while j < m:
            res[d] = arr2[j]
            d += 1
            j += 1
        return res[k-1]


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
