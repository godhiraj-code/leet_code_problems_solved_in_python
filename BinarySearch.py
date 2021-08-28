# order agnostic binary search
# Problem link : https://leetcode.com/problems/binary-search/
"""
    When a problem statement has something like sorted array , first thing that should come to your mind
    should be applying Binary Search.
    The below code is an implementation of a binary search.
    In Binary Search, 3 things are important
    1. Find the start and end range .
    2. Find the mid value.
    3. Based on the comparison of target value and mid value, reduce the search space
    The complexity of binary search is : O(log n)
"""


def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    is_asc = nums[start] < nums[end]

    while start <= end:
        mid = int(start + (end - start) / 2)
        if nums[mid] == target:
            return mid
        if is_asc:
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return - 1


# nums = [-1,0,3,5,9,12]
# target = 9
# print(binary_search(nums, target))
