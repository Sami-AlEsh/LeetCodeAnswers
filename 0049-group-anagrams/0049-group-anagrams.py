from collections import defaultdict, Counter

class Solution:
    def hash(self, s):
        result = [0] * 26
        d = Counter(s)
        for c in d.keys():
            result[ord(c)-ord('a')] = d[c]
        return str(result)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: list())
        for s in strs:
            d[self.hash(s)].append(s)

        return list(d.values())