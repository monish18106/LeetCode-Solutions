class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        cur = 1
        ans = 0
        n = len(s)
        for i in range(1,n):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans += min(prev,cur)
                prev = cur
                cur = 1
        ans += min(prev,cur)
        return ans