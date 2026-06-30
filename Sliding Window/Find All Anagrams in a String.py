class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = [0]*26
        b = [0]*26
        c = []
        p1 = len(p)
        s1 = len(s)
        if p1 > s1:
            return []
        for i in range(p1):
            a[ord(p[i]) - ord('a')] += 1
            b[ord(s[i]) - ord('a')] += 1
        if a == b:
            c.append(0)

        for i in range(p1,s1):
            b[ord(s[i]) - ord('a')] += 1
            b[ord(s[i-p1]) - ord('a')] -= 1
            if a == b:
                c.append(i-p1+1)
        return c