class Solution:
    def countSegments(self, s: str) -> int:
        s = list(filter(lambda x: x.strip() != "", s.split(' ')))
        return len(s) if s != "" else 0