class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):     # subsets count: 2^n == 1 << n
            cur = []
            for j in range(n):      # each j is a possible candidate for this subset
                if i & (1 << j):    # we should add j to the current subset
                    cur.append(nums[j])
            res.append(cur)
        return res