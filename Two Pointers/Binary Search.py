class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            l = 0
            h = len(nums) - 1
            while l <= h:
                m = (l+h)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m+1
                else:
                    h = m-1

        