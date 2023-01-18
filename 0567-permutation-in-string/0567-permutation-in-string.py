from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        length = len(s1)
        current = dict()
        
        s = 0
        for e in range(len(s2)):
            current[s2[e]] = current.get(s2[e], 0) + 1
            
            if e - s + 1 > length :
                current[s2[s]] -= 1
                if current[s2[s]] == 0:
                    del current[s2[s]] 
                s += 1
            
            if e - s + 1 == length and d == current:
                return True
        return False