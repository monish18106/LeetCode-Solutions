class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        b = int(0)
        for i in accounts:
            c = int(0)
            for a in i:
                c += a
            if c > b:
                b = c
        return b