class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = b = nums[0]
        for i in range(1,len(nums)):
            c = max(nums[i],c+nums[i])
            b = max(c,b)
        return b