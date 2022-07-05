import math


def findNthRootOfM(n, m):
    low = 1
    high = n
    eps = 0.0000006

    while((high-low) > eps):
        mid = (low+high) / 2
        if(multiply(mid, n) < m):
            low = mid
        else:
            high = mid
    return math.ceil(low)


def multiply(number, n):
    ans = 1
    for i in range(n):
        ans = ans * number
    return ans
