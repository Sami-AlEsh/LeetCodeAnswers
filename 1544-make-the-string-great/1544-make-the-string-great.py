class Solution:
    def makeGood(self, s: str) -> str:
        def is_not_good(c1, c2):
            return (c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper())
        
        stack = []
        for c in s:
            if stack and stack[-1].lower() == c.lower() and is_not_good(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)