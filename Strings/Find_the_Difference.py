
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i in s:
            i = ord(i)
        for i in t:
            i = ord(i)
        if sum(s) != sum(t):
            return chr(abs(sum(s) - sum(t)))

