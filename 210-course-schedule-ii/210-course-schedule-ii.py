from collections import defaultdict


class Solution:
    def list_to_dict(self, ls):
        d = defaultdict(lambda: list())
        for pair in ls: d[pair[0]].append(pair[1])
        return d
    
    def dfs(self, course, prereq, visited, cycle, output):
        if course in cycle: return False
        if course in visited: return True
        
        cycle.add(course)
        for pre in prereq[course]:
            if not self.dfs(pre, prereq, visited, cycle, output): return False
        cycle.remove(course)
        visited.add(course)
        output.append(course)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = self.list_to_dict(prerequisites)
        output = []
        visited, cycle = set(), set()
        for course in range(numCourses):
            if not self.dfs(course, prereq, visited, cycle, output): return []
        return output
        