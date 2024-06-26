'''
Problem: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sorting numbers so we do not repeat the solution
        # complexity becomes O(nlogn)
        nums = sorted(nums)
        result = []
        for i, first_num in enumerate(nums):
            # To avoid starting out with the same number
            if i > 0 and nums[i-1]==first_num:
                continue

            # left starts one position after the current pointer and right at the end of the list
            l, r = i + 1, len(nums)-1
            while l < r:
                total = first_num + nums[l] + nums[r]
                if total>0:
                    r -= 1
                elif total<0:
                    l += 1
                else:
                    result.append([first_num, nums[l], nums[r]])
                    # ensure that we capture all combinations having the same starting point (first_num)
                    # however the second number cannot be the same as the current left
                    # therefore we increment left and ensure that it is not the same as the previous
                    l += 1
                    while nums[l]== nums[l-1] and l<r:
                        l += 1
        return result
    
# Time complexity is computed in 2 parts             
# A. The solution above uses sorting which has a complexity of O(nlogn)
# B. There's one outer loop that goes through all nums O(n), and one more inner loop that uses two pointer method with complexity O(n)
# Therefore the total complexity becomes O(nlogn) + O(n**2) which is O(n**2)
# If one were to use brute force method, the complexity would have been O(n**3)

'''
Time complexity: O(n**2)
Space complexity: O(1)
'''

        