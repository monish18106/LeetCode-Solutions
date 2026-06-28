class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = c = 0
        m = len(g)
        n = len(s)
        g.sort()
        s.sort()
        while i < m and j < n:
            if s[j] >= g[i]:
                c += 1
                i += 1
                j += 1
            else:
                j += 1
        return c