class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, current):
            if current >= len(word):
                return True

            if not (0<=row<len(board)) or not (0<=col<len(board[0])):
                return False

            if word[current] != board[row][col] or board[row][col] == '#':
                return False
            
            board[row][col] = '#'
            if dfs(row+1, col, current+1): return True
            if dfs(row, col+1, current+1): return True
            if dfs(row-1, col, current+1): return True
            if dfs(row, col-1,current+1): return True
            board[row][col] = word[current]

            return False

        for r, row in enumerate(board):
            for c, num in enumerate(row):
                if dfs(r,c,0):
                    return True


        return False

