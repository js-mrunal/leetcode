'''
Problem: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

# Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        source_hash, target_hash = {}, {}
        for i, w in enumerate(s):
            source_hash[w] = 1 + source_hash.get(w, 0)
            target_hash[t[i]] = 1 + target_hash.get(t[i], 0)

        return source_hash==target_hash

'''
Time Complexity: O(n)
Space Complexity: O(2n) -> O(n)
'''

# Solution 2 using in-built functions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)