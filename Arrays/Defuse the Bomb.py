class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        b = []        
        if k == 0:
            return [0]*n
        elif k >0:
            for i in range(len(code)):
                c = 0
                for j in range(i,i+k):
                    c += code[(j+1)%n]
                b.append(c)
        elif k < 0:
            for i in range(len(code)):
                c = 0
                for j in range(i,i+k,-1):
                    c += code[(j-1+n)%n]
                b.append(c)
        return b
    



        