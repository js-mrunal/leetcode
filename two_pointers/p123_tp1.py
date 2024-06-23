'''
Problem: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize the left and right pointer to the
        # start and end of the string
        left, right = 0, len(s)-1

        # change the string to lowercase
        s = s.lower()
        while left < right:
            # while s[left] is not ASCII - increment the left pointer
            while ((not s[left].isalnum()) and (left< right)):
                left += 1
            while ((not s[right].isalnum()) and (right>left)):
                right -= 1
            if s[left]!=s[right]:
                return False
            left, right = left + 1, right - 1
        return True
    
'''
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:

    def isPalindrome(self, s: str) -> bool:
        # Initialize the left and right pointer to the
        # start and end of the string
        left, right = 0, len(s)-1
        # change the string to lowercase
        s = s.lower()
        s = "".join(x for x in s if x.isalnum())
        return s==s[::-1]