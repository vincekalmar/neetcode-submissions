class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        


        nums.sort()
        res = []
        def dfs(i, tally, sub):

            if tally >= target:
                if tally == target:
                    res.append(sub.copy())
                    return
            
            for j in range(i, len(nums)):
                if tally + nums[j] > target:
                    return
                
                sub.append(nums[j])
                dfs(j, tally + nums[j], sub)
                sub.pop()

        dfs(0,0,[])
        return res
