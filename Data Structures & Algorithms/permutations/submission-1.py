class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(start):
            if start == len(nums) - 1:
                res.append(nums.copy())
                return 

            for current in range(start, len(nums)):

                nums[current], nums[start] = nums[start], nums[current]
                dfs(start+1)
                nums[current], nums[start] = nums[start], nums[current]
        dfs(0)
        return res