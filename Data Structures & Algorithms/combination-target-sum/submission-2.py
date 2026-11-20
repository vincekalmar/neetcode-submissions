class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        def dfs(i, total, sub):
            if total > target or i >= len(nums):
                return
            
            if total == target:
                res.append(sub.copy())
                return 
            
            sub.append(nums[i])
            dfs(i, total + nums[i], sub)
            sub.pop()
            dfs(i+1, total, sub)


        dfs(0,0,[])        
        return res
