from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) > len(s): s, t = t, s
        d = Counter(s) - Counter(t)
        return list(d.keys())[0]
        