def insertion(a):
    n = len(a)
    for i in range(n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = key

    return a


print(insertion([2, 5, 6, 1]))
# We can use heap to optimize thn TC, now TC -> O(NK)
