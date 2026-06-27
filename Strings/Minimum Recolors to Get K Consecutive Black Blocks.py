class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        c = 0
        for i in range(k):
            if blocks[i] == 'W':
                c += 1
        mi = c
        for i in range(k,n):
            if blocks[i] == 'W':
                c += 1
            if blocks[i-k] == 'W':
                c -= 1
            mi = min(c,mi)
        return mi
            