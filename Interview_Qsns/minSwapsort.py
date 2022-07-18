
# Complete the minimumSwaps function below.
def minimumSwaps(arr, n):
    swap = 0
    for i in range(0, n):
        while arr[i] != (i+1):
            t = arr[i] - 1
            arr[t], arr[i] = arr[i], arr[t]
            swap += 1
    return swap
