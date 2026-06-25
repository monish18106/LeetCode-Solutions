class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m= 0 
        l = 0
        r = 0
        z = 0
        n = len(nums)
        while l < n:
            if nums[l] == 0:
                z += 1
            m = max(m, abs(l-r+1))
            while z > k:
                if a[r] == 0:
                    z -= 1
                r += 1
            l += 1
        return m