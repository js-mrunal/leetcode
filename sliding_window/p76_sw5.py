'''
Problem: 76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        # create a map of need i.e. count of the target which needs to be met
        t_hash = {}
        for char in t:
            t_hash[char] = 1 + t_hash.get(char, 0)
        
        left, right = 0, 0
        window = {}
        matching, min_length = 0, float("infinity")
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            if s[right] in t_hash and window[s[right]] == t_hash[s[right]]:
                matching += 1
            # if we have found a window that contains all the elements of target
            # we can shift the left pointer so that we find a minimum window
            # we keep shifting the left pointer till the matching condition is no longer valid.
            while matching==len(t_hash):
                # since we have found a possible result, we can check against current minimum
                if len(s[left:right]) < min_length:
                    min_length = len(s[left:right])
                    pointer_tuple = left, right

                if s[left] in t_hash and window[s[left]] == t_hash[s[left]]:
                    matching -= 1

                window[s[left]] -= 1
                left += 1

        if min_length != float("infinity"):
            l,r = pointer_tuple
            return s[l:r+1]
        return ""        
    

'''
Time complexity: O(n)
Space complexity: O(n)
'''