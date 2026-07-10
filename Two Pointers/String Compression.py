class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        w = 0
        i = 0
        while i < n:
            ch = chars[i]
            c = 0
            while i < n and chars[i] == ch:
                c += 1
                i += 1
            chars[w] = ch
            w += 1
            if c > 1:
                for d in str(c):
                    chars[w] = d
                    w += 1
        return w