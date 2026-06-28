class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        n = j//2
        s = list(s)
        while i < j:
            if s[i] in "AEIOUaieou" and s[j] in "AEIOUaeiou":
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            if s[j] not in "AEIOUaeiou":
                j -= 1
            if s[i] not in "AEIOUaeiou":
                i += 1
        return "".join(s)


        