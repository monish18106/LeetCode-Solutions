class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = []
        ans = []
        a = [False]*len(nums)
        n = len(nums)
        def bt():
            if len(s) == n:
                ans.append(s[:])
                return
            for i in range(n):
                if a[i]:
                    continue
                a[i] = True
                s.append(nums[i])
                bt()
                s.pop()
                a[i] = False
        bt()
        return ans
