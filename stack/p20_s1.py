'''
Problem: 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # create a dictionary keeping track of valid sets of parantheses
        valid_pairs = {')':'(', ']':'[', '}':'{'}
        ds_stack = []
        for bracket in s:
            # if the character is closing paranthesis and len of stack is greater than zero
            # then pop the stack top
            if bracket in valid_pairs and len(ds_stack)>0:
                stack_top = ds_stack.pop()
                if stack_top != valid_pairs[bracket]:
                    return False
            # else we push any of the characters to the stack
            else:
                ds_stack.append(bracket)
        # important: to check if there are still any unmatched pairs of parantheses
        return len(ds_stack)==0
    
'''
Time complexity: O(n)
Space complexity = O(n)
'''
        