class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n+1

        for i, num in enumerate(nums):
            index = abs(num) - 1
            if 0 <= index < n and nums[index] > 0:
                nums[index] *= -1

        for i in range(0, n):
            if nums[i] > 0:
                return i+1

        return n+1
