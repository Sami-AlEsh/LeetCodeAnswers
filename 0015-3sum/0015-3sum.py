class Solution:
    def __init__(self):
        self.triplets = []
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i in range(len(nums)):
            # skip same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]: continue
            self.search_pair(nums, i)
        return self.triplets
    
    def search_pair(self, arr, target_index):
        target_sum = -arr[target_index]
        left = target_index + 1
        right = len(arr) - 1
        while(left < right):
            if left == target_index: 
                left += 1
                continue
            if right == target_index:
                right -= 1
                continue
            
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:  # found the triplet
                self.triplets.append(sorted([-target_sum, arr[left], arr[right]]))
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1  # skip same element to avoid duplicate triplets
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1  # skip same element to avoid duplicate triplets
            elif target_sum > current_sum:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum