class Solution:
    def removeDuplicates(self, s: str) -> str:        
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            if len(stack) > 0 and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == 2:
                    stack.pop()
            else:
                stack.append([s[i], 1])
        return ''.join(map(lambda t: t[0], stack))