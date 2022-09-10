class Solution:
    def countSegments(self, s: str) -> int:
        if s == "": return 0
        
        no_space = True if s[0] != ' ' else False
        cnt = 0
        for i, c in enumerate(s):
            if no_space and c == ' ':
                no_space = not no_space
                cnt += 1
            elif not no_space and c != ' ':
                no_space = not no_space
        return cnt + 1 if s[-1] != ' ' else cnt
    
        # Easier (slower) solution
        #s = list(filter(lambda x: x.strip() != "", s.split(' ')))
        #return len(s) if s != "" else 0