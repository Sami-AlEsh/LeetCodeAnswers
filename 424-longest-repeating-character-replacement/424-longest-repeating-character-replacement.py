class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, _max, maxfreq = 0, 0, 0
        d = {}
        for end in range(len(s)):
            d[s[end]] = d.get(s[end], 0) + 1
            
            maxfreq = max(maxfreq, d[s[end]])
            
            while (end - start + 1 - maxfreq) > k:
                d[s[start]] -= 1
                if d[s[start]] == 0: del d[s[start]]
                start += 1
            _max = max(_max, end - start + 1)
            
        return _max