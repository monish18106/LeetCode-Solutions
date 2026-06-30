class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        l = 0
        mf = 0
        a = 0
        for r in range(len(s)):
            c[s[r]] = c.get(s[r],0) + 1
            mf = max(mf, c[s[r]])

            while (r-l+1) - mf > k:
                c[s[l]] -= 1
                l += 1
            a = max(a,r-l+1)
        return a
