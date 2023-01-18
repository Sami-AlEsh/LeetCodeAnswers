class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2: return len(fruits)
        
        s, m_items = 0, 0
        bucket = dict()
        
        for e in range(len(fruits)):
            bucket[fruits[e]] = bucket.get(fruits[e], 0) + 1
            
            while len(bucket) > 2:
                bucket[fruits[s]] -= 1
                if bucket[fruits[s]] == 0:
                    del bucket[fruits[s]]
                s += 1
            
            m_items = max(m_items, e - s + 1)
        return m_items