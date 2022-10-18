class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            # skip same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                current_sum = nums[i] + nums[left] + nums[right]
                
                # we need a pair with a bigger sum
                if current_sum > 0:
                    right -= 1
                
                # we need a pair with a smaller sum
                elif current_sum < 0:
                    left += 1
                    
                # found the triplet
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    # skip same element to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]: left += 1
            
        return triplets        