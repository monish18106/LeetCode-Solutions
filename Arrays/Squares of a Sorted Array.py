class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = [0]*len(nums)
        l = 0
        r = len(nums)-1
        p = r 
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                a[p] = nums[l]*nums[l]
                l+=1
            else:
                a[p] = nums[r]*nums[r]
                r -= 1
            
            p -= 1
        
        return a 



