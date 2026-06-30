class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        an = []
        s = []

        def bt(i):
            if len(nums) == i:
                an.append(s[:])
                return
            s.append(nums[i])
            bt(i+1)
            s.pop()
            bt(i+1) 

        bt(0)
        return an
        