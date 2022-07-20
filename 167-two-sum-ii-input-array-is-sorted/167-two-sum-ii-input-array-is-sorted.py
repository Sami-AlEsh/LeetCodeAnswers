from collections import defaultdict

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers)-1
        while start <= end:
            mid = ( start + end ) // 2
            pairs = numbers[start] + numbers[end]
            
            if target == pairs:
                return [start+1, end+1]
            
            elif target > pairs:
                start = mid + 1 if numbers[mid] + numbers[end] < target else start + 1
            
            else:
                end = mid - 1 if numbers[start] + numbers[mid] > target else end - 1