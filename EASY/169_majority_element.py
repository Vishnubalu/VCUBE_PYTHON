from typing import List

"""
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    

Example 1:

    Input: nums = [3,2,3]
    Output: 3
Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hashtable = {}
#         for num in nums:
#             hashtable[num] = hashtable.get(num, 0) + 1
#             if hashtable[num] > len(nums)/2:
#                 return num


def majorityElement(self, nums: List[int]) -> int:
    count = 0
    elem = 0
    for i in nums:
        if count == 0:
            elem = i
        if elem == i:
            count += 1
        else:
            count -= 1
    print(elem)