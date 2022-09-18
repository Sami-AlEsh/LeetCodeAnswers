from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)]  for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j]
                
                if i == 0 and j == 0: continue
                
                s = set()
                if j > 0: s.add(dp[i][j-1])
                if i > 0: s.add(dp[i-1][j])
                    
                dp[i][j] += min(s)
        return dp[-1][-1]