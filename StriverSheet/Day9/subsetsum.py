from typing import List


def subset(i, sum, num, ans):
    if i == len(num):
        ans.append(sum)
        return
    subset(i+1, sum+num[i], num, ans)
    subset(i+1, sum, num, ans)


def subsetSum(num: List[int]) -> List[int]:
    ans = []
    subset(0, 0, num, ans)
    ans.sort()
    return ans
