class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        setForCol = defaultdict(set)
        setForBox = defaultdict(set)

        for r, row in enumerate(board):
            setForRow = set()
            for c, num in enumerate(row):
                if num == '.':
                    continue

                x = r // 3
                y = c // 3

                if num in setForRow or num in setForCol[c] or num in setForBox[(x,y)]:
                    return False
                
                setForRow.add(num)
                setForCol[c].add(num)
                setForBox[(x,y)].add(num)


        return True