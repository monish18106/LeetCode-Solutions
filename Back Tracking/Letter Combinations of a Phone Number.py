class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        b = []
        def bt(s):
            if len(b) == k:
                ans.append(b[:])
                return
            for i in range(s,n+1):
                if i in b:
                    continue
                b.append(i)
                bt(i)
                b.pop()
        
        bt(1)
        return ans