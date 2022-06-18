def compare(a):
    return a[1] / a[0]


def maximumValue(items, n, w):
    # Sort the values in reverse based on ratio
    items = sorted(items, key=compare, reverse=True)

    maxVal = 0
    curWei = 0

    for i in range(n):
        if curWei + items[i][0] <= w:
            curWei += items[i][0]
            maxVal += items[i][1]
        else:
            remWei = w - curWei
            maxVal += items[i][1] * (remWei/items[i][0])
            break
    return round(maxVal, 2)
