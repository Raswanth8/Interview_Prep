# User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        visited = [[0]*n for i in range(n)]
        res = []

        def backtrack(i, j, stack):
            if not((i >= 0 and i < n and j >= 0 and j < n and not visited[i][j] and m[i][j] == 1)):
                return

            if (i == n-1 and j == n-1):
                res.append(stack)
                return

            visited[i][j] = 1

            moves = [[i+1, j, 'D'], [i, j+1, 'R'],
                     [i-1, j, 'U'], [i, j-1, 'L']]

            for x, y, s in moves:
                backtrack(x, y, stack+s)

            visited[i][j] = 0

        backtrack(0, 0, "")
        return res
