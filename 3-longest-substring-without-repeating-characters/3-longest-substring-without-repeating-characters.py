class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        _max = 0
        unique = set()
        for end in range(len(s)):
            if s[end] not in unique:
                #print(f'{s[end]} added')
                unique.add(s[end])
            
            else:
                while s[end] in unique:
                    #print(f'{s[start]} removed')
                    unique.remove(s[start])
                    start += 1
                unique.add(s[end])
            
            #print(s[start:end+1], ', set:', unique)
            _max = max(_max, len(unique))
        
        return _max