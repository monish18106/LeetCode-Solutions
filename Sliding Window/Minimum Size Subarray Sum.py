class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        c = 0
        ans = 10**9
        n = len(nums)
        for i in range(n):
            c += nums[i]

            while c >= target:
                ans = min(ans,i-l+1)
                c -= nums[l]
                l += 1
        if ans == 10**9:
            return 0

        return ans
            

            
            
        