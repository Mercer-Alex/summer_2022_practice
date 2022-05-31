
def two_sum(num_list, target):
    tempdict = {}

    for i, x in enumerate(num_list):
        temp = target - x
        if tempdict.get(temp, -1) != -1:
            return tempdict.get(temp), i

        tempdict[x] = i


nums = [2, 7, 11, 15]
goal = 9

nums2 = [-1, -2, -3, -4, -5]
goal2 = -8

nums3 = [3, 2, 95, 4, -3]
goal3 = 92

print(two_sum(nums, goal))

print(two_sum(nums2, goal2))

print(two_sum(nums3, goal3))
