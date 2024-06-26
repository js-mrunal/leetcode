'''
Problem: 128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

# One obvious way to solve this problem is by sorting the array 
# The complexity of sorting is O(nlogn) 
# But the problem statement says :: "You must write an algorithm that runs in O(n) time."

# To tackle this problem we will create a set from the list
# we will then iterate through the list and check if the number has left-neighbour
# by left-neighbour we mean - if (num-1) is present in the set
# if (num-1) is not present in the set; it means num is the start of the sequence

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        # iterate tthrough the nums
        for n in nums:
            # check if the number n is start of the sequence
            # i.e. if it has left neighbor
            if n-1 not in nums_set:
                continue
            # if it is start of the sequence then 
            # check how compute the current streak
            curr_seq = 1
            while (n + curr_seq) in nums_set:
                curr_seq += 1
            longest_seq = max(longest_seq, curr_seq)
        return longest_seq

'''
Time complexity: O(n)
Space complexity: O(n)
'''
# This solution uses a dictionary where each key represents a number from the input array, 
# and its corresponding value indicates the length of a consecutive sequence with that number 
# as either the upper or lower bound of the sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # removing duplicates is crucial so that 
        # we do not overaccount sequence lengths
        nums = set(nums)
        sequence_table = {}
        maxseq = 0
        for n in nums:
            # check if previous_num is start/end of previously detected sequence
            prev_seq = sequence_table.get(n-1, 0)
            # check if next_num is start/end of previously detected sequence
            next_seq = sequence_table.get(n+1, 0)
            # total sequence length 
            val = prev_seq + next_seq + 1
            # update start/end of the sequence with sequence length
            sequence_table[n-prev_seq] = val
            sequence_table[n+next_seq] = val
            maxseq = max(maxseq, val)
        return maxseq


'''
Time complexity: O(n)
Space complexity: O(n)
'''