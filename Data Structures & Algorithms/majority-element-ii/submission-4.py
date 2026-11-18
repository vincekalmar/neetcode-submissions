class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
         
        cand1, cand2 = None, None
        count1, count2 = 0, 0 

        for num in nums:
            if count1 == 0 or cand1 == num:
                cand1 = num
                count1 += 1
            elif count2 == 0 or cand2 == num:
                cand2 = num
                count2 +=1
            else:
                count1-=1
                count2-=1
        
        count1, count2 = 0, 0 
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
        res = []

        if count1 > len(nums)/3: res.append(cand1)
        if count2 > len(nums)/3: res.append(cand2)

        return res
