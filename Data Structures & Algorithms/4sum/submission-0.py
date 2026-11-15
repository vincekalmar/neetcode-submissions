class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        previ = None 
        prevj = None
        res = []

        for i in range(n):
            if nums[i] == previ:
                    continue
            previ = nums[i]
            for j in range(i+1, n):

                if nums[j] == prevj:
                    continue
                
                prevj = nums[j]

                l, r = j + 1, n - 1
                
                t = target - nums[i] - nums[j]

                while l < r:

                    sm = nums[l] + nums[r]

                    if sm > t:
                        r-=1
                    elif sm < t:
                        l+=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        temp = nums[r]
                        while l < r and nums[r] == temp:
                            r-=1
        return res




