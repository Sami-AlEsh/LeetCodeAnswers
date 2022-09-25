from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        elif p == "": return [i for i in range(len(s))]
        
        s1 = dict(Counter(p))
        s2 = dict(Counter(s[:len(p)]))
        
        l = 0
        poses = []
        if s1 == s2: poses.append(0)
        
        for r in range(len(p), len(s)):
            s2[s[r]] = s2.get(s[r], 0) + 1
            s2[s[l]] -= 1
            if s2[s[l]] == 0: del s2[s[l]]
            l += 1
            
            if s1 == s2: poses.append(l)
            
        return poses
            
            
            
            
            
            
            
            
            
            
            

        