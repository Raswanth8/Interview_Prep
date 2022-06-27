def func1(num):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            continue
        elif int(num[i]) % 2 == 1:
            # increment the digit by 1 and make remaining digits as '0'
            num = num[:i] + str(int(num[i]) + 1) + '0' * (len(num) - i - 1)
    return int(num)


def func2(num):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            continue
        elif int(num[i]) % 2 == 1:
            # decrement the digit by 1 and make remaining digits as '8'
            num = num[:i] + str(int(num[i]) - 1) + '8' * (len(num) - i - 1)
    return int(num)


def trueN(num):
    a = abs(func1(num) - num)
    b = abs(func2(num) - num)
    res = min(a, b)
    return res


print(trueN(4178))
