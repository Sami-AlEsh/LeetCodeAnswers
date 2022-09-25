class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s , _max, ones = 0, 0, 0
        
        for e in range(len(nums)):
            ones += 1 if nums[e] == 1 else 0
            
            while (e-s+1 - ones) > k:
                ones -= 1 if nums[s] == 1 else 0
                s += 1
            
            _max = max(_max, e-s+1)
        
        return _max