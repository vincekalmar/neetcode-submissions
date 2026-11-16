class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or i >= len(word) or word[i] != board[r][c]:
                return False
            
            if i == len(word) - 1 and word[i] == board[r][c]:
                return True

            temp = board[r][c]
            board[r][c] = '#'
            dir = [(-1,0), (1,0), (0,1), (0,-1)]

            for x, y in dir:
                if dfs(i+1,r+x, c+y):
                    return True
            board[r][c] = temp
            return False


        for row in range(len(board)):

            for col in range(len(board[row])):

                if board[row][col] == word[0]:
                    seen = set()
                    if dfs(0,row,col):
                        return True
        return False


