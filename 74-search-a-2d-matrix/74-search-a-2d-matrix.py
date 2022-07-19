class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    
        start = 0
        end = len(matrix)-1
        while start <= end:
            mid = (start + end) // 2
            row = matrix[mid]
            print('mid: ', mid)

            if row[0] <= target <= row[-1]:
                
                _start = 0
                _end = len(row) - 1
                
                while _start <= _end:
                    _mid = (_start + _end) // 2
                    print('_mid: ', _mid)
                    value = matrix[mid][_mid]
                    if target == value:
                        return True
                    elif target > value:
                        _start = _mid + 1
                    else:
                        _end = _mid - 1
                    # print(_start, _end)
                
                return False

            elif target > row[-1]:
                start = mid + 1

            else:    
                end = mid - 1  

        return False





