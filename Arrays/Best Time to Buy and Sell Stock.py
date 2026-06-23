class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        p = mx = int(0)
        for i in prices:
            if i < l:
                l = i
            else:
                mx = max(mx, i-l)
        return mx


        