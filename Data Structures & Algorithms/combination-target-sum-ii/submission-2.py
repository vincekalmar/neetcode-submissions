class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start, tally, combo):
            if tally > target:
                return
            elif tally == target:
                res.append(combo.copy())

            
            for current in range(start, len(candidates)):
                if start != current and candidates[current] == candidates[current-1]:
                    continue
                
                combo.append(candidates[current])
                dfs(current+1, tally+candidates[current], combo)
                combo.pop()
        dfs(0,0,[])
        return res
