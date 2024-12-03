# Approach:
# The n-queens problem can be solved using backtracking. We place a queen in a row, ensuring that it
# does not conflict with any other queen. We keep track of columns, diagonals, and the current row to 
# ensure that no two queens threaten each other. The base case is when all queens have been placed 
# successfully. If we can place all queens without conflicts, we save the configuration as a solution.

# Time Complexity: O(N!), where N is the size of the board. In the worst case, we try placing queens 
# in each of the N rows, and for each row, we check N possible positions (with pruning).
# Space Complexity: O(N), where N is the size of the board. The recursion stack uses O(N) space,
# and we store N columns and diagonals during backtracking.

# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No, the approach is standard backtracking.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Result list to store all solutions
        result = []
        
        # Helper function for backtracking
        def backtrack(row, columns, diag1, diag2, board):
            # If we have placed queens in all rows, add the board configuration to result
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            # Try all column positions for the current row
            for col in range(n):
                # Check if the column or diagonals are attacked
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place the queen and mark the column and diagonals
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                
                # Recursively place queens in the next row
                backtrack(row + 1, columns, diag1, diag2, board)
                
                # Backtrack: remove the queen and unmark the column and diagonals
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = '.'
        
        # Initialize board with empty spaces
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        # Sets to keep track of attacked columns and diagonals
        columns = set()
        diag1 = set()  # row - col diagonal
        diag2 = set()  # row + col diagonal
        
        # Start the backtracking process from row 0
        backtrack(0, columns, diag1, diag2, board)
        
        return result

