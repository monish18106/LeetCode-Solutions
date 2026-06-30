class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        return max(d, key = d.get)