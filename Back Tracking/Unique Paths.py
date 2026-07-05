class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 0
        dp = [[-1]*n for _ in range(m)]
        def bt(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = bt(i,j+1) + bt(i+1,j)
            
            return dp[i][j]
        
        return bt(0,0)
        