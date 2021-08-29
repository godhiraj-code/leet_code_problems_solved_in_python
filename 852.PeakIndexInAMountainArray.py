# Problem link: https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
"""


def peak_index_in_a_mountain_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = int(start + (end - start) / 2)
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start


print(peak_index_in_a_mountain_array([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
