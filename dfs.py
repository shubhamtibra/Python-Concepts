class Solution:
    def exist(self, board, word):
        self.R = len(board)
        self.C = len(board[0])
        self.board = board
        
        for i in range(self.R):
            for j in range(self.C):
                if self.dfs(i, j, word):
                    return True
        
        return False
    
    def dfs(self, i, j, word):
        if len(word) == 0:
            return True
        
        if (i < 0 or i >= self.R or 
            j < 0 or j >= self.C or 
            self.board[i][j] != word[0]):
            return False
        
        temp = self.board[i][j]
        self.board[i][j] = '#'  # mark as visited
        
        result = (self.dfs(i+1, j, word[1:]) or
                  self.dfs(i-1, j, word[1:]) or
                  self.dfs(i, j+1, word[1:]) or
                  self.dfs(i, j-1, word[1:]))
        
        self.board[i][j] = temp  # restore the cell
        
        return result

# Driver code
if __name__ == '__main__':
    solution = Solution()
    
    # Test case 1
    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word1 = "ABCCED"
    print(solution.exist(board1, word1))  # Expected output: True
    
    # Test case 2
    board2 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word2 = "SEE"
    print(solution.exist(board2, word2))  # Expected output: True
    word3 = "ABCED"
    print(solution.exist(board2, word3))
    print(solution.exist(board2, "ABC"))