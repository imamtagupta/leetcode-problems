
########################################
# 79. Word Search     #
########################################

# leetcode link: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        flag = False
        for i in range(row):
            for j in range(col):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != word[0]:
            return False
        
        save = board[i][j]
        board[i][j] = '*'
        temp = self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i, j-1, word[1:]) or self.dfs(board, i, j+1, word[1:])
        board[i][j] = save
        return temp