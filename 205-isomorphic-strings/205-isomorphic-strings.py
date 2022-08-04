class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:        
        d1 = dict()
        d2 = dict()
        for i, c in enumerate(s):
            d1[c] = d1.get(c, t[i])
            d2[t[i]] = d2.get(t[i], c)

            if d1[c] != t[i] or d2[t[i]] != c: return False
        return True