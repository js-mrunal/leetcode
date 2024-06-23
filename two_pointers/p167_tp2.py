'''
Problem: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # In this solution we use the fact that array is "sorted" to our advantage
        # initialise the left and right to the start and end of the array 
        left, right = 0, len(numbers)-1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return left+1, right+1
            # if the sum is less than target - then we shift the left pointer (include a bigger number in combination)
            if curr_sum<target:
                left+=1
            # else the sum is greater than target and we shift the right pointer
            else:
                right-=1

'''
Time complexity: O(n)
Space complexity: O(1)
'''
        