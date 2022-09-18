from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #dp = [[0 for _ in range(n)]  for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                #dp[i][j] = grid[i][j]
                
                if i == 0 and j == 0: continue
                    
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i][j-1]
        
        return grid[-1][-1]