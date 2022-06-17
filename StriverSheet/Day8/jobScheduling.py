def jobScheduling(jobs):
    maxDeadline, maxProfit = 0, 0
    # Sort based on Decreasing order of profit with job
    jobs.sort(key=lambda x: (-x[1], -x[0]))

    for i in range(0, len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i][0])

    slots = [False] * (maxDeadline+1)

    for i in range(len(jobs)):
        x = jobs[i][0]
        while x > 0:
            if slots[x] == False:
                maxProfit = maxProfit + jobs[i][1]
                slots[x] = True
                break
            x -= 1
    return maxProfit
