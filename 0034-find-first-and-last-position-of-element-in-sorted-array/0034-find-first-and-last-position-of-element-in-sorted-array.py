class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bst(get_last):
            index = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (end + start) // 2

                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    index = mid
                    if get_last: start = mid + 1
                    else: end = mid - 1
            return index
        
        return [bst(False), bst(True)]