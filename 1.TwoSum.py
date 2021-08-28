#  Problem link: https://leetcode.com/problems/two-sum/


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
    Approach to solve the problem. 
    One of the easier way is to compare every element with other element , for example, 
    for array 2, 7, 11, 15  and target = target,
    compare 2 with 7 , 11, 15 etc 
    and then 7 with 11, 15 and so on... 
    
    Better way : 
    create a map of value and it's corresponding index  and check 
    if the target - value is present in the map, if present then that will mean we got our answer . 
    if not then update the map 
"""


def twoSum(nums, target):
    val_key_pair = {}
    for i, v in enumerate(nums):
        if target - v in val_key_pair:
            return [val_key_pair[target - v], i]
        val_key_pair[v] = i
    return


nums = [2, 7, 11, 15]
print(twoSum(nums, 9))
