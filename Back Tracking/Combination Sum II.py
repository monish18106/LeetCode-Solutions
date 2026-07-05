class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        t = []
        ans = []
        n = len(candidates)
        def bt(i,curr):
            if curr == target:
                ans.append(t[:])
                return
            if curr > target:
                return
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]: 
                    continue
                t.append(candidates[j])
                bt(j+1, curr + candidates[j])
                t.pop()

        bt(0,0)
        return ans