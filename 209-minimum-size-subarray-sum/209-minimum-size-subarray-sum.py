import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, tot, _min = 0, 0, math.inf
        for e in range(len(nums)):
            tot += nums[e]
            
            while tot >= target:
                _min = min(_min, e-s+1)
                tot -= nums[s]
                s += 1
        return _min if _min != math.inf else 0