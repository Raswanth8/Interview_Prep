import sys
sys.setrecursionlimit(1000)


def myfunc(s):
    res = []
    part = []

    def backtrack(i):
        if i >= len(s):
            res.append(part[::])
            return

        for j in range(len(s)):
            if s[:j+1] == s[:j+1][::-1]:
                part.append(s[:j+1])
                backtrack(j+1)
                part.pop()

    backtrack(0)
    return res


print(myfunc('aab'))
