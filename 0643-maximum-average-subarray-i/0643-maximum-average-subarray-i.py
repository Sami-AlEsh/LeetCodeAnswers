from math import inf
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Edge cases
        if k > len(nums):
            return sum(nums) / len(nums)
        
        # Solution
        m_avg = -inf
        _sum = 0.0
        s = 0
        
        for e in range(len(nums)):
            _sum += nums[e]
            
            if e >= k - 1:
                m_avg = max(m_avg, _sum / k)
                _sum -= nums[s]
                s += 1
                
        return m_avg
                
                
        