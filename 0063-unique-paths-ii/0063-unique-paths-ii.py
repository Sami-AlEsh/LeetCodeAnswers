class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[None for _ in range(m)] for _ in range(n)]
        
        # Edge case
        if obstacleGrid[0][0] == 1: return 0
        
        # Fill first column
        value = 1
        for i in range(n):
            if obstacleGrid[i][0] == 1: 
                value = 0
            obstacleGrid[i][0] = value
            
        # Fill first row
        value = 1
        for j in range(1, m):
            if obstacleGrid[0][j] == 1: 
                value = 0
            obstacleGrid[0][j] = value
        
        # DP method
        def dp(i, j):
            if i == 0 or j == 0 :
                return obstacleGrid[i][j]
            
            elif obstacleGrid[i][j] == 1:
                return 0
            
            if memo[i][j] is None:
                memo[i][j] = dp(i, j-1) + dp(i-1, j)
            
            return memo[i][j]
        
        return dp(n-1, m-1)
        