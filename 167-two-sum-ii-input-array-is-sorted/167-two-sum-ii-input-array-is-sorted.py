class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, num in enumerate(numbers):
            if num not in d: d[num] = list()
            d[num].append(i+1)
        
        for n in numbers:
            if target - n in d:
                return [d[n].pop(0), d[target-n].pop(0)]