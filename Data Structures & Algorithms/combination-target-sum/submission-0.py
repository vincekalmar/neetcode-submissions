class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def dfs(i, tally, sub):
            if i >= len(nums):
                return 
            if tally >= target:
                if tally == target:
                    res.append(sub.copy())
                return

            sub.append(nums[i])
            dfs(i, tally + nums[i], sub)
            sub.pop()
            dfs(i+1, tally, sub)

        dfs(0,0,[])
        return res



