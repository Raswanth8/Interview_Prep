# Tiger Analytics Interview Question
from sortedcontainers import SortedList
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        output = []

        for n in nums[::-1]:
            res = SortedList.bisect_left(s, n)
            output.append(res)
            s.add(n)

        return output[::-1]

# Sorted List is a sorted mutable sequence in python
