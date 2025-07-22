# 0036 Valid Sudoku - Medium
# https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. 
# Tags: Array | Hash Table | Matrix

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       rows = [set() for _ in range(9)]
       cols = [set() for _ in range(9)]
       boxes = [set() for _ in range(9)]

       for i in range(9):
           for j in range(9):
               num = board[i][j]

               if num == ".":
                    continue
               box_index = (i // 3) * 3 + (j // 3)

               if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
               rows[i].add(num)
               cols[j].add(num)
               boxes[box_index].add(num)
       return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidRow(["8","3","3",".","7",".",".",".","."]))