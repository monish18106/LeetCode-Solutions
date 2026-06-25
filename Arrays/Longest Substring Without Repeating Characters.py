class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        for i in range(len(s)):
            seen = set()
            d = 0
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    d += 1
                mx = max(d,mx)
        return mx