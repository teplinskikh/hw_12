import random


def sort_list(nums):
    nums = nums.copy()
    n = len(nums)
    cnt = 0
    swaps = 0
    avoided_swaps = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            cnt += 1
            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
            swaps += 1
        else:
            avoided_swaps += 1

    return nums, cnt, swaps, avoided_swaps


lst_1 = [3, 47, 24, 0, -7]
lst_2 = [15, 2, 10, 8, 34, 5, 11, 33, 5, -6]

n = int(input())
lst_3 = []

for i in range(n):
    lst_3.append(random.randint(0, 100))

for numbers in [lst_1, lst_2, lst_3]:
    result, cnt, swaps, avoided_swaps = sort_list(numbers)

    print("Sorted list:", result)
    print("Comparisons:", cnt)
    print("Swaps:", swaps)
    print("Avoided swaps:", avoided_swaps)
    print()

