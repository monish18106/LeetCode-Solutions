class Solution:
    def sortColors(self, nums: List[int]) -> None:
        j = 0
        for i in range(3):
            for k in range(len(nums)):
                if nums[k] == i:
                    nums[k],nums[j] = nums[j],nums[k]
                    j +=1
        
            
        