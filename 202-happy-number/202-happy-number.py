class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n in visited: return False
            if n == 1: return True
            visited.add(n)
            n = sum([ int(i)**2 for i in str(n)])