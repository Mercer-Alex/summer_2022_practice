def max_sub(nums):
    newNum = currMax = nums[0]

    for x in range(1, len(nums)):
        newNum = max(nums[x], nums[x] + newNum)
        currMax = max(currMax, newNum)

    return currMax


numbs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub(numbs))
