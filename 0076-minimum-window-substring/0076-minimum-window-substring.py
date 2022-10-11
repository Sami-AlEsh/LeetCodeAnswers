class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def _index(c):
            if c.isupper(): return 25 + ord(c) - ord('A')
            else: return ord(c) - ord('a')

        s1, s2 = t, s
        if s1 == "": return ""
        if len(s1) > len(s2): return ""
        
        s1_count, s2_count = [0] * 52, [0] * 52
        for i in range(len(s1)):
            s1_count[_index(s1[i])] += 1
            
        matches = 0
        for i in range(52):
            matches += 1 if s1_count[i] == s2_count[i] else 0
        s = 0
        _min = ""
        for e in range(len(s2)):
            index = _index(s2[e])
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1

            while matches >= 52:
                _min = s2[s:e+1] if len(s2[s:e+1]) < len(_min) or _min == "" else _min
                index = _index(s2[s])
                s2_count[index] -= 1
                if s1_count[index] - 1 == s2_count[index]:
                    matches -= 1
                s += 1

        return _min
