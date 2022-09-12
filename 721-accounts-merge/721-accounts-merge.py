from collections import deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        q = deque([])
        for a in accounts: q.append([a[0], set(a[1:])])
        
        res = []
        while q:
            cur = q.popleft()
            if cur[0] == '*':
                continue
    
            is_merged = False
            for account in q:
                if not cur[1].isdisjoint(account[1]):
                    is_merged = True
                    cur[1] |= account[1]
                    account[0] = '*'
            
            if is_merged: q.append(cur)
            else: res.append(cur)

        return map(lambda account: [account[0]] + sorted(list(account[1])), res)
