class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s)-1
        s = list(s)
        while i < j:
            if not (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122):
                i += 1
            elif not (65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122):
                j -= 1
            else:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
        return "".join(s)

        