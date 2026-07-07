class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        xr = 0
        def bt(ind, xcurr):
            nonlocal xr
            if ind == n:
                xr += xcurr
                return
            bt(ind+1,xcurr)
            bt(ind+1, xcurr ^ nums[ind])
        bt(0,0)
        return xr


