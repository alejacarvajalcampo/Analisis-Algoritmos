class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )

            board[r][c] = temp

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False