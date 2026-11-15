class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_mp = defaultdict(set) # maps column to its set
        grid_mp = defaultdict(set) # maps grid to its set

        for row, ROW in enumerate(board):
            row_set = set()

            for col, num in enumerate(ROW):
                if num == '.':
                    continue

                if num in row_set:
                    return False

                if num in col_mp[col]:
                    return False

                x, y = row // 3, col // 3

                if num in grid_mp[(x,y)]:
                    return False
                
                row_set.add(num)
                col_mp[col].add(num)
                grid_mp[(x,y)].add(num)

        return True

                
                

