from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        single = False
        for k, v in Counter(s).items():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                if not single: 
                    length += 1
                    single = True
        return length