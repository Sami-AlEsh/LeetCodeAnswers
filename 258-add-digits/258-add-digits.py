class Solution:
    def addDigits(self, num: int) -> int:
        def combine_digits(num):
            count = 0
            for d in str(num):
                count += int(d)
            return count
        
        res = combine_digits(num)
        while(len(str(res)) > 1):
            res = combine_digits(res)
        return res