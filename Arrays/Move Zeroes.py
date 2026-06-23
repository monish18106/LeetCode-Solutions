class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = int(0)
        if len(nums) == 1 and nums[0] == 0:
            pass
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == 0:
                    nums.pop(i)
                    c += 1
            for i in range(c):
                nums.append(0)