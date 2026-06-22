
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        s = list(s)
        for i in s:
            i = ord(i)
        for i in t:
            i = ord(i)
        s.sort()
        t.sort()
        if s == t:
            return True
        else:
            return False




