class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        t = 0
        sx = sy = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    sx,sy = i,j
                if grid[i][j] != -1:
                    t += 1
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        ans = 0

        def bt(i,j,count):
            nonlocal ans
            if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                if count == t:
                    ans += 1
                return
            temp = grid[i][j]
            grid[i][j] = -1
            for dx,dy in d:
                bt(i+dx , j+dy , count + 1)
            grid[i][j] = temp

        bt(sx,sy,1)
        return ans