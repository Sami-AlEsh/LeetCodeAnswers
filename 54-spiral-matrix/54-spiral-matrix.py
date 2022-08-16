class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def turn(d):
            if d == 'r': return 'd' 
            elif d == 'd': return 'l' 
            elif d == 'l': return 'u' 
            else: return 'r'
        
        def nextt(d, i, j):
            if d == 'r': return i, j+1
            elif d == 'd': return i+1, j
            elif d == 'l': return i, j-1
            else: return i-1, j
        
        def valid(matrix, i, j, n, m):
            if i >= 0 and i < n and j >= 0 and j < m and matrix[i][j] != -200:
                return True
            else:
                return False
        
        d = 'r' # r - d - l - u
        n = len(matrix)
        m = len(matrix[0])
        
        result = [matrix[0][0]]
        matrix[0][0] = -200
        i = 0
        j = 0
        
        for _ in range(n*m-1):
            _i, _j = nextt(d, i, j)
            if not valid(matrix, _i, _j, n, m):
                d = turn(d)
                _i, _j = nextt(d, i, j)
            i, j = _i, _j
            result.append(matrix[i][j])
            matrix[i][j] = -200
        
        
        return result
        