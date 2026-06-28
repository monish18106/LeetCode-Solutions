class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f = f""
        i = j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                f += word1[i]
                f += word2[j]
            elif i >= len(word1):
                f += word2[j]
            else:
                f += word1[i]
            i += 1
            j += 1
        return f


