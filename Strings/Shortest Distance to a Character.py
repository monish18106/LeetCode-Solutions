class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a = []
        for i in range(len(s)):
            if s[i] == c:
                a.append(i)
        b = []
        for i in range(len(s)):
            n = 10**9
            for j in a:
                n = min(n,abs(i-j))
            b.append(n)

                
        return b


                
        