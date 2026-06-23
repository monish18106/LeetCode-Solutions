class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = mx = 0
        for n in nums:
            if n == 1:
                c += 1
                mx = max(mx,c)
            else:
                c = 0
        return mx
