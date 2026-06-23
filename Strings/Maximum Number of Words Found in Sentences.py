class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = b = int(0)
        for i in sentences:
            a = list(map(str, i.split()))
            c = len(a)
            if c > b :
                b = c
        return b

        