'''
Problem: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
from typing import List
from collections import defaultdict

# Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for s in strs:
            character_map = [0]*26
            for c in s:
                character_map[ord(c)-ord('a')] += 1
            hash_table[tuple(character_map)].append(s)
        return list(hash_table.values())
    

'''
Time complexity: O(m * n * 26) {m: number of strings, n: average length of each string} -> O(m.n)
Space complexity: O(m.n)
'''