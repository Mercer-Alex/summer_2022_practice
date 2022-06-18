def isBadVersion(n):
    return n >= 4

def firstBadVersion(n):
    start = 1
    end = n

    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid
            else:
                end = mid
        else:
            start = mid

print(firstBadVersion(10))


