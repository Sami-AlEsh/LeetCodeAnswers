class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "": return True
        if len(s1) > len(s2): return False
        
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1
            
        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0
        
        s = 0
        for e in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[e]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            
            index = ord(s2[s]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            s += 1
        return matches == 26
            