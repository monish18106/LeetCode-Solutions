class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        c = []

        def bt(oc,cc):
            if len(c) == 2*n:
                a.append("".join(c))
                return
            if oc < n:
                c.append("(")
                bt(oc + 1,cc)
                c.pop()
            if cc < oc:
                c.append(")")
                bt(oc, cc + 1)
                c.pop()
        bt(0,0)
        return a