class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1

        total = 0
        res = 0
        for num in nums:

            total += num

            if total - k in mp:
                res += mp[total-k]

            mp[total] += 1

        return res
            


        # 2, 1, 2, 4




        