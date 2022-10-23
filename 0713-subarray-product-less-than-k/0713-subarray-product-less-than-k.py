class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while (product >= k and left <= right):
                product /= nums[left]
                left += 1
            result += right - left + 1
        return result