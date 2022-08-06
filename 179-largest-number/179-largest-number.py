class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums = self.mergesort(nums)
        return str(int("".join(nums)))
    
    def compare(self, n1, n2):
        return n1 + n2 > n2 + n1
    
    def mergesort(self, nums):
        length = len(nums)
        if length < 2: return nums
    
        mid = length // 2
        left_list = self.mergesort(nums[:mid])
        right_list = self.mergesort(nums[mid:])
        return self.merge(left_list, right_list)
        
    def merge(self,l1,l2):
        result = []
        while l1 and l2:
            if self.compare(l1[0],l2[0]):
                result.append(l1[0])
                l1.pop(0)
            else:
                result.append(l2[0])
                l2.pop(0)
        result.extend(l1 or l2)
        return result