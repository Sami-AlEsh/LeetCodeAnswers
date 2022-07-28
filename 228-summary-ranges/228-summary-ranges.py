class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1: return []
        
        ans= []
        cur_pair = [str(nums[0])]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1 :
                if str(nums[i-1]) != cur_pair[-1]:
                    cur_pair.append(str(nums[i-1]))
                ans.append(cur_pair)
                cur_pair = [str(nums[i])]
        
        if cur_pair[-1] != str(nums[-1]):
            cur_pair.append(str(nums[-1]))
        ans.append(cur_pair)
        
        return [ str("->".join(p)) for p in ans ]
            
                  
            