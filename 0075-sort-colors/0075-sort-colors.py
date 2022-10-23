class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, low, high = 0, 0, len(nums) - 1
        
        while i <= high:
            # 0 : Swap with low
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            
            # 1 : Keep Moving
            elif nums[i] == 1:
                i += 1
            
            # 2 : Swap with High
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                