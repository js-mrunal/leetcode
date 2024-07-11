'''
Problem: 567. Permutations in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # simplest rule: if length(s2) is smaller
        # then it cannot have length(s1)
        if len(s2) < len(s1):
            return False

        s1_hash, s2_hash = [0]*26, [0]*26
        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_hash[i] == s2_hash[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2), 1):
            if matches == 26:
                return True
            # slide window from left and right
            # deal with right index first
            index = ord(s2[right]) - ord('a')
            s2_hash[index] += 1
            # does adding 1 from right disturb the equality/matches we had previously
            if s2_hash[index] - 1 == s1_hash[index]:
                matches -= 1
            # does adding 1 element from right add to the matches
            elif s2_hash[index] == s1_hash[index]:
                matches += 1
            
            # dealing with the left index. - shifting left by 1
            index = ord(s2[left]) - ord('a')
            s2_hash[index] -= 1
            # does removing 1 from left disturb the equality/matches we had previously
            if s2_hash[index] + 1 == s1_hash[index]:
                matches -= 1
            # does removing 1 element from left help matches
            elif s2_hash[index] == s1_hash[index]:
                matches += 1
            left += 1
        return matches == 26

'''
Time complexity: O(n)
Space complexity: O(26n) -> O(n)
'''
        

        

        