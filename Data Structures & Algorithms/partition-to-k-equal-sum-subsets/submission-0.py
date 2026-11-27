class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)

        if total % k != 0: return False

        target = total // k

        nums.sort()

        partition = [0] * k

        def dfs(current):
            if current == len(nums):
                return True
            

            for i in range(k):
                if partition[i] + nums[current] <= target:
                    partition[i] += nums[current]

                    if dfs(current + 1):
                        return True
                    
                    partition[i] -= nums[current]

                if partition[i] == 0:
                    break

            return False
        
        return dfs(0)
