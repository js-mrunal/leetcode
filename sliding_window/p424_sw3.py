'''
Problem: 424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # In this solution for every substring, we are checking
        # if it is valid i.e. length of substring - most_freq_elem <= k
        most_freq, max_length = 0, 0
        left = 0
        count_char = {}
        # we are going to start from the left and expand the window 
        # to the right till the window is valid
        for right, right_char in enumerate(s):   
            count_char[right_char] = 1 + count_char.get(right_char, 0)
            # most freq can be the element to which we have
            # added the count
            most_freq = max(most_freq, count_char[right_char])
            # if the number of replacements required in the string are
            # more than k i.e window is invalid then shrink the window from left
            if ((right - left)+1 - most_freq) > k:
                count_char[s[left]] -= 1
                left += 1
            # update max length
            max_length = max((right-left)+1, max_length)
        return max_length
'''
Time complexity: O(n)
Space complexity: O(n)
'''