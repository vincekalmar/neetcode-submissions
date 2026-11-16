class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, len(nums)):

                nums[j], nums[i] = nums[i], nums[j]
                dfs(i+1)
                nums[j], nums[i] = nums[i], nums[j]
        dfs(0)
        return res

#    i = 0
#    j = 0
#    nums[1,2,3]
#        i=1
#        j=1
#        nums[1,2,3]
#            i=2
#            j=2
#            nums[1,2,3]
                
    
