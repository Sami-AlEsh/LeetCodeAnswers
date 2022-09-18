class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        _max = 0
        unique = set()
        
        for end in range(len(s)):
            while s[end] in unique:
                unique.remove(s[start])
                start += 1
            unique.add(s[end])
            _max = max(_max, end-start+1)
        
        return _max