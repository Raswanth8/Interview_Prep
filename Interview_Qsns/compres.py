def compress(s):
    n = len(s)
    count = 1
    res = ""
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            res += s[i-1]
            if count > 1:
                res += str(count)
            count = 1
    res += s[-1]
    if count > 1:
        res += str(count)
    return res


print(compress("aabbcc"))
