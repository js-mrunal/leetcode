'''
Problem 84: Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ds_stack = []
        # each element in the stack would be a tuple (starting_point, h)
        # indicating the starting point and height of each element

        # maintain a monotonically increasing stack
        max_area = 0
        for idx, h in enumerate(heights):
            bar_pos = idx
            while ds_stack and ds_stack[-1][1] > h:
                # logic to pop element and compute max area
                bar_pos, bar_height = ds_stack.pop()
                max_area = max(max_area, (idx - bar_pos) * bar_height)
            ds_stack.append((bar_pos, h))
        # account for area computed by bars that are extended till the end
        while ds_stack:
            bar_pos, bar_height = ds_stack.pop()
            max_area = max(max_area, (len(heights) - bar_pos) * bar_height)
        return max_area
