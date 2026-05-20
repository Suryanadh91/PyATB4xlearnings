def two_sum_bruteforce(nums, target):
    # check every pair (i, j) with j > i
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    # problem guarantees one solution, but return None defensively
    return None

print(two_sum_bruteforce([1, 2, 3, 4], 9))


