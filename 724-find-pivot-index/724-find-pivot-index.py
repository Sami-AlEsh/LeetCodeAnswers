class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return True
        
        def prefix_sum(nums):
            s = 0
            for i in range(len(nums)):
                s += nums[i]
                nums[i] = s
        
        prefix_sum(nums)
        print(nums)
        for i in range(len(nums)):
            left = nums[i-1] if i > 0 else 0
            right = nums[-1]-nums[i] if i < length - 1 else 0
            if left == right:
                return i
        
        return -1
                