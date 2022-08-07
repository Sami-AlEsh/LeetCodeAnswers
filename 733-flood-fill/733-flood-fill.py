def dfs(img, i, j, n, m, visited, base_color, color):
    if 0 <= i < n and 0 <= j < m:
        key = str(i) + str(j)
        if key in visited or img[i][j] != base_color : return

        img[i][j] = color
        visited.add(key)
        dfs(img, i+1, j, n, m, visited, base_color, color)
        dfs(img, i-1, j, n, m, visited, base_color, color)
        dfs(img, i, j+1, n, m, visited, base_color, color)
        dfs(img, i, j-1, n, m, visited, base_color, color)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dfs(image, sr, sc, len(image), len(image[0]), set(), image[sr][sc], color)
        return image