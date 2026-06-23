class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)//2
        i = 0
        j = len(s)-1
        while i < n:
            s[i],s[j] = s[j],s[i]
            i += 1 
            j -=1
        