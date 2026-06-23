class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f = [True]*len(words)
        for i in words:
            k = len(i)-1
            for j in range(len(i)//2):
                if i[j] != i[k]:
                    f[words.index(i)] = False
                    break
                k -= 1
        g = True
        for i in range(len(f)):
            if f[i]:
                g = False
                return words[i] 
        if g:
            return ""

            
        