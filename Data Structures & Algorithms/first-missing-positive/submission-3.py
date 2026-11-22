class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i, num in enumerate(nums):
            index = abs(num) - 1
            if index < 0 or index >= n:
                continue
            if nums[index] < 0:
                continue
            nums[index] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1