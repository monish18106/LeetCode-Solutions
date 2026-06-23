class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        a = [1]*n
        for i in range(n):
            a[i] = p
            p *= nums[i]
        s = 1
        for i in range(n-1,-1,-1):
            a[i] *= s
            s *= nums[i]
        return a 


