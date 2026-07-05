class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        t = []
        ans = []

        def bt(i,curr):
            if curr == target:
                ans.append(t[:])
                return
            if curr > target or i == len(candidates):
                return
            t.append(candidates[i])
            bt(i,curr + candidates[i])
            t.pop()
            bt(i+1 , curr)

        bt(0,0)
        return ans

        