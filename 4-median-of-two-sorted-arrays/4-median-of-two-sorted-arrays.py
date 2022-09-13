class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def _merge(nums1, nums2):
            l1 = len(nums1)
            l2 = len(nums2)
            merged = [-1] * (l1+l2)
            index, i, j = 0, 0, 0
            while i < l1 and j < l2:
                if nums1[i] < nums2[j]:
                    merged[index] = nums1[i]
                    i += 1
                else:
                    merged[index] = nums2[j]
                    j += 1
                index += 1

            # Copy the rest of left part if exist
            while i < l1:
                merged[index] = nums1[i]
                i += 1
                index += 1

            # Copy the rest of right part if exist
            while j < l2:
                merged[index] = nums2[j]
                j += 1
                index += 1

            return merged

        def merge_sort(nums):
            length = len(nums)
            if length < 2: return nums

            mid = length // 2
            return _merge(merge_sort(nums[0:mid]), merge_sort(nums[mid:]))

        nums = merge_sort(nums1 + nums2)
        
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[mid] + nums[mid-1]) / 2
        else:
            return nums[mid]

