class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def dfs(start, sub):
            res.append(sub.copy())

            for current in range(start, len(nums)):
                if current != start and nums[current] == nums[current-1]:
                    continue
                sub.append(nums[current])
                dfs(current+1, sub)
                sub.pop()

        dfs(0,[])
        return res
