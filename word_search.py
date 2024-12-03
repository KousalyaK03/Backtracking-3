# Approach:
# The solution is still based on backtracking, but with additional pruning techniques:
# 1. If the remaining part of the word is too long to fit within the remaining grid, we stop early.
# 2. If the first character of the word doesn't match the cell we start from, we avoid unnecessary searches.
# 3. We prune unnecessary exploration by using a set to track visited positions to avoid revisiting.

# Time Complexity: O(m * n * 4^L) in the worst case, but pruning improves average performance.
# Space Complexity: O(m * n) due to recursion stack and visited cells storage.

# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No, these improvements follow standard optimization techniques.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Helper function for backtracking
        def backtrack(i, j, index):
            # If we've matched all letters in the word, return True
            if index == len(word):
                return True
            
            # Check bounds and if the current cell matches the word's current character
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            # Temporarily mark the current cell as visited
            temp, board[i][j] = board[i][j], '#'
            
            # Explore all 4 possible directions (up, down, left, right)
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # Recursively search for the next character in the word
                if backtrack(i + x, j + y, index + 1):
                    return True
            
            # Unmark the current cell (backtrack)
            board[i][j] = temp
            return False
        
        # Early pruning check: Only start backtracking if the first letter of the word exists in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # If the character matches the first character of the word, start backtracking
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        
        return False
