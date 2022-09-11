class Solution:
    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i+1, j)
        return 1
        
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += self.dfs(grid, i, j)
        return cnt