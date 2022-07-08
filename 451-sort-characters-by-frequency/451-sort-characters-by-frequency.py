from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        d = Counter(s)
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)

        for k in d:
            ans += k[0] * k[1]
        return ans
            