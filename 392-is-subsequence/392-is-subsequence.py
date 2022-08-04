class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for c in s:
            try:
                while c != t[index]: index += 1
                index += 1
            except:
                return False
        
        return True
            