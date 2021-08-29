# Problem link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


"""

"""
Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
"""


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return arr[start % len(arr)]


def nextGreatestLetter(letters, target):
    val = binary_search(letters, target)
    print(val)


letters = ["c", "f", "j"]
target = "j"
nextGreatestLetter(letters, target)
