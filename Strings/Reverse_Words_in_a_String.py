
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        b = s[::-1]
        return " ".join(b)
