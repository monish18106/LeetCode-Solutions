class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = sum(nums[:k])
        mx = w
        for i in range(k,len(nums)):
            w += nums[i] 
            w -= nums[i-k]
            mx = max(mx,w)
        return mx/k