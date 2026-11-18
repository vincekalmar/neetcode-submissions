class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = None 
        count = 0

        for num in nums:
           
            if count == 0 or candidate == num:
                candidate = num
                count += 1 

            if candidate != num:
                count -= 1
            

        
        return candidate
