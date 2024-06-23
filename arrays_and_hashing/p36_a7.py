'''
Problem: Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # maintain a dictionary to keep track 
        # of characters found in rows, cols and sub-boxes
        row_characters = defaultdict(set)
        col_characters = defaultdict(set)
        box_characters = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                # check if the character is numeric 
                if board[r][c].isnumeric():
                    if (board[r][c] in row_characters[r] or
                        board[r][c] in col_characters[c] or 
                        board[r][c] in box_characters[r//3,c//3]):
                        # returning False if we found a character that 
                        # is repeated either in row, col or sub-boxes
                        return False
                    row_characters[r].add(board[r][c])
                    col_characters[c].add(board[r][c])
                    box_characters[r//3, c//3].add(board[r][c])
                    
        return True
    
'''
Time Complexity: O(n**2)
Space Complexity: O(n)
'''