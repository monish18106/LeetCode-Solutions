class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        k = len(nums)
        if k not in nums:
            return k
        else:
            for i in range(k):
                if i == nums[i]:
                    pass
                else:
                    return i
                    break
        

        