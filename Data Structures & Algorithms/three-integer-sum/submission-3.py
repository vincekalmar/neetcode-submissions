class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = None
        for i, num in enumerate(nums):
            
            l, r = i + 1, len(nums) - 1
            target = -num
            
            if nums[i] == prev:
                continue
            prev = nums[i]

            while l < r:
                sm = nums[l] + nums[r]

                if sm > target:
                    r -= 1
                elif sm < target:
                    l += 1
                else:
                    res.append([-target, nums[l], nums[r]])
                    temp = nums[r]
                    while r > l and nums[r] == temp:
                        r-=1

        return res