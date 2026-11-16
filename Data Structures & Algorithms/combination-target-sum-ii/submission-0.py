class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        1,2,2,4,5,6,9


        candidates.sort()
        res = []

        def dfs(i, tally, sub):

            if tally >= target:
                if tally == target:
                    res.append(sub.copy())
                    return
            
            for j in range(i, len(candidates)):
                if i != j and candidates[j-1] == candidates[j]:
                    continue
                if tally + candidates[j] > target:
                    return
                
                sub.append(candidates[j])
                dfs(j+1, tally + candidates[j], sub)
                sub.pop()
        
        dfs(0,0,[])

        return res