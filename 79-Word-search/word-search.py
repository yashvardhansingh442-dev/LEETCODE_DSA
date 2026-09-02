class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'  # mark as visited

            found = (backtrack(r + 1, c, i + 1) or
                     backtrack(r - 1, c, i + 1) or
                     backtrack(r, c + 1, i + 1) or
                     backtrack(r, c - 1, i + 1))

            board[r][c] = temp  # backtrack
            return found

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False
