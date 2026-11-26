class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        def dfs(start):
            if start == len(nums) - 1:
                res.append(nums.copy())
                return


            for current in range(start, len(nums)):
                if current != start and nums[current] == nums[start]:
                    continue

                nums[current], nums[start] = nums[start], nums[current]
                dfs(start+1)

            for current in range(len(nums) - 1, start, -1):
                nums[current], nums[start] = nums[start], nums[current]

        dfs(0)
        return res