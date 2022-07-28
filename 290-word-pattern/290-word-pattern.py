class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s): return False
        
        d = dict()
        d2 = dict()
        for c,w in zip(pattern, s):
            if c not in d and w not in d2:
                d[c] = w
                d2[w] = c
            
            elif (c in d and d[c] != w) or (w in d2 and d2[w] != c):
                return False
            
        return True
