class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(nums)
        s2 = {i for i in range(1, len(nums)+1)}
        return list(s2 - s1)