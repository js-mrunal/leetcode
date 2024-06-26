'''
Problem: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
'''

# 1. When will the water accumulate?
# Water will start accumulating at "low-lying" areas
# we define the low-lying area that has higher height on both sides

# 2. How much water will accumulate?
# For position i :
# accumulated water = min(max_height_left, max_height_right) - height_i
# if accumulated_water > 0 then add it to the sum

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left_height, right_height = [0]*len(height), [0]*len(height)

        # Compute maximum height to the left of the position i
        max_left, max_right = 0, 0
        for left in range(len(height)):
            left_height[left] = max_left
            if height[left] > max_left:
                max_left = height[left]

        # Compute maximum height to the right of the position i
        for right in range(len(height)-1, -1, -1):
            right_height[right] = max_right
            if height[right] > max_right:
                max_right = height[right]

        # How much water will accumulate
        total_water = 0
        for i in range(len(height)):
            water_level = min(left_height[i], right_height[i]) - height[i]   
            total_water += max(0, water_level)
        return total_water  

'''
Time complexity = O(3n) -> O(n)
Space complexity = O(2n) -> O(n)
'''

# how to solve by two pointer method?
class Solution:
    def trap(self, height: List[int]) -> int:
        # Using two pointer method by initialising left and right
        # to the start and the end of array height
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        total_water = 0
        while left <= right:
            # when we have a right side bounded by a height
            # that is larger than height on left on a position i 
            # we can conclude that water can possibly accumulate at position 
            # depending on the height at position i 
            if max_left < max_right:
                # how much water will be accumulated? 
                water_level = max_left - height[left]
                max_left = max(max_left, height[left])
                left += 1
            # same as above but for position on the right
            else:
                water_level = max_right - height[right]
                max_right = max(max_right, height[right])
                right -= 1
            total_water += max(0, water_level)
        return total_water  
    

'''
In the solution above, we can skip the operation of max(0, water_level) if we change the order of statements in if-else clause
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        total_water = 0
        while left <= right:
            if max_left < max_right:
                # how much water will be accumulated? 
                # changing the order of how we compute max_left helps to
                # ensure water_level at every position >= 0
                max_left = max(max_left, height[left])
                water_level = max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                water_level = max_right - height[right]
                right -= 1
            total_water += water_level
        return total_water  
    
'''
Time complexity: O(n)
Space complexity: O(1)
'''