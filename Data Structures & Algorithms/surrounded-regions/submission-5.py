class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        X = [[True] * COL for _ in range(ROW)]
        q = deque()

        for r in range(ROW):
            if board[r][0] == 'O':
                q.append((r,0))
            if board[r][COL-1] == 'O':
                q.append((r,COL-1))
        for c in range(COL):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[ROW-1][c] == 'O':
                q.append((ROW-1, c))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        print(q)
        while q:
            x, y = q.popleft()

            if not X[x][y]:
                continue

            X[x][y] = False
            print(x, " ", y, " ", X[x][y])
            for xd, yd in dirs:
                r, c = x+xd, y+yd

                if 0<=r<ROW and 0<=c<COL and board[r][c] == 'O' and X[r][c]:
                    q.append((r,c))
            


        for r, row in enumerate(board):
            for c, col in enumerate(board[0]):
                if X[r][c]:
                    board[r][c] = 'X'
                