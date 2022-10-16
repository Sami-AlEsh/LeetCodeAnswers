class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        cur_ptr, next_ptr = 0, 0
        
        while next_ptr < length:
            nums[cur_ptr] = nums[next_ptr]
            while next_ptr < length and nums[cur_ptr] == nums[next_ptr]:
                next_ptr += 1
            cur_ptr += 1
        
        return cur_ptr