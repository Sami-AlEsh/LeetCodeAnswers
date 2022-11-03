class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length = 0
        lookup = dict()
        
        for s in words:
            if s in lookup:
                length += 4
                lookup[s] -= 1
                if lookup[s] == 0:
                    del lookup[s]
            else:
                key = str(s[1]+s[0])
                lookup[key] = lookup.get(key, 0) + 1
            
        for key in lookup:
            if key[0] == key[1]:
                length += 2
                break
            
        return length