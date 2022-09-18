from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s = 0
        _max = 0
        d = dict()
        for e in range(len(fruits)):
            d[fruits[e]] = d.get(fruits[e], 0) + 1

            while len(d) > 2:
                d[fruits[s]] -= 1
                if d[fruits[s]] == 0:
                    del d[fruits[s]]
                s += 1

            _max = max(_max, e-s+1)

        return _max
    