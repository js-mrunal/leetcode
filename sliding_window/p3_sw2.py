'''
Problem: 3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # maintain a hash table to keep a track of when we last saw
        # the element
        last_seen_at = {}
        left, max_len = 0, 1
        for right, right_char in enumerate(s):
            # when we encounter a duplicated element 
            # we start shrinking our window from the left
            if right_char in last_seen_at:
                left = max(last_seen_at[right_char]+1, left)
            last_seen_at[right_char] = right
            max_len = max(right-left+1, max_len)
        return max_len

        
'''
Time complexity: O(n)
Space complexity: O(n)
'''