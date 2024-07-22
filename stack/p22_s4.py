'''
Problem 22. Generate Parenthesis

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ds_stack = []
        results = []
        def generate_paranthesis_backtrack(open_n: int, close_n: int):
            # valid if and only if open_n == close_n == n
            if open_n == close_n == n:
                results.append("".join(ds_stack))
                return 
            # add open parenthesis only if open_n < n 
            if open_n < n:
                ds_stack.append("(")
                generate_paranthesis_backtrack(open_n + 1, close_n)
                ds_stack.pop()
            # add closing parenthesis only if close_n < open_n
            if close_n < open_n:
                ds_stack.append(")")
                generate_paranthesis_backtrack(open_n, close_n + 1)
                ds_stack.pop()
            
        generate_paranthesis_backtrack(open_n = 0, close_n = 0)
        return results