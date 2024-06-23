'''
Problem: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''
from typing import List

# Solution 1:
# Create a dictionary and sort by values 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maintain a count dictionary keep track of frequency for each element in the array
        num_to_count = {}
        for n in nums:
            num_to_count[n] = num_to_count.get(n,0) + 1

        num_to_count = {k1:v1 for k1, v1 in sorted(num_to_count.items(), key=lambda item: item[1], reverse=True)}
        return list(num_to_count.keys())[:k]
    

'''
Time complexity of sorting in best case is 0(nlogn) where n is the array's size
'''

'''
Follow up: How to make algorithm better than O(nlogn)?
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maintain a count dictionary keep track of frequency for each element in the array
        num_to_count = {}
        for n in nums:
            num_to_count[n] = num_to_count.get(n,0) + 1

        # the maximum number of times a num can repeat itself is
        # the length of the nums array
        count_tracker = [[] for i in range(len(nums)+1)]

        # for each count how many nums do we have?
        for num, count in num_to_count.items():
            count_tracker[count].append(num)

        # parse the count_tracker from reverse till we have k most frequent nums
        # result to keep a track of elements 
        result = []
        for count in range(len(count_tracker)-1, 0, -1):
            for elem in count_tracker[count]:
                result.append(elem)
            if len(result) == k:
                return result
            
'''
Using heaps to solve the problem

Time complexity: O(n) + O(n) + O(n) -> O(n)
Space complexity: O(n)
'''
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        for n in nums:
            num_to_count[n] = num_to_count.get(n,0) + 1

        # create a heap
        # Heaps are binary trees for which every parent node 
        # has a value less than or equal to any of its children. 
        heap = []
        for num, count in num_to_count.items():
            heapq.heappush(heap, (count, num))
            # if the length of heap is higher than 
            # number of elements then we perform heap pop which 
            # will pop the smallest element
            if len(heap) > k:
                heapq.heappop(heap)

        # result to keep a track of elements 
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result