'''
Problem: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

from typing import List

# Initial solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = {}, {}

        # maintain a prefix array which contains 
        # prefix multiplication for every position
        pre = 1
        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]

        # maintain a postfix array which contains 
        # postfix multiplication for every position
        post = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post
            post *= nums[i]

        result = [prefix[i]*postfix[i] for i in range(len(nums))]
        return result
    
'''
Time complexity: O(n)
Space complexity: O(n)
'''
    

# We can reduce the storage in above solution by maintaining
# only one array, result.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        result = {}
        for left in range(len(nums)):
            result[left] = prefix
            prefix *= nums[left]

        for right in range(len(nums)-1, -1, -1):
            result[right] = postfix
            postfix *= nums[right]

        return result 
    
'''
Time complexity: O(n)
Space complexity: O(1) -- output array does not count as extra memory
'''
    