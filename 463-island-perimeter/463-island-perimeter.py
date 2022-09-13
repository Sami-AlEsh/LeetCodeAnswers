class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length = len(grid)
        length2 = len(grid[0])
        
        def check_side(i, j):
            if i < 0 or i >= length:
                return 1
            elif j < 0 or j >= length2:
                return 1
            elif grid[i][j] == 0:
                return 1
            else:
                return 0
        
        edges = 0
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        for i in range(length):
            for j in range(length2):
                if grid[i][j] == 1:
                    for ii, jj in directions:
                        edges += check_side(i+ii, j+jj)
        return edges