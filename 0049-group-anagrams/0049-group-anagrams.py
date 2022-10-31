from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: list())
        for s in strs:
            d[''.join(sorted(s))].append(s)

        return list(d.values())