import math
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref_sum = [0] * len(nums)
        cnt = 0
        for i in range(len(nums)):
            cnt += nums[i]
            pref_sum[i] = cnt
        
        _index = -1
        _min = math.inf
        for i in range(len(pref_sum)):
            left_side = int((pref_sum[i]) / (i + 1))
            try:
                right_side = int((pref_sum[-1] - pref_sum[i]) / (len(pref_sum) - (i + 1)))
            except:
                right_side = 0
            avg = abs(left_side - right_side)
            if avg < _min:
                _min = avg
                _index = i
        return _index
            