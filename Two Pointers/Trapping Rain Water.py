class Solution:
    def trap(self, height: List[int]) -> int:
        ml = 0
        mr = 0
        l = 0
        r = len(height)-1
        w = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > ml:
                    ml = height[l]
                else:
                    w += ml - height[l]
                    l += 1
            else:
                if height[r] > mr:
                    mr = height[r]
                else:
                    w += mr - height[r]
                    r -= 1
        return w
        