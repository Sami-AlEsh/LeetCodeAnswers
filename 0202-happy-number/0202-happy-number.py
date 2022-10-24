class Solution:
    def find_square_sum(self, num):
        _sum = 0
        while (num > 0):
            digit = num % 10
            _sum += digit * digit
            num //= 10
        return _sum
    
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.find_square_sum(slow)  # move one step
            fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
            if slow == fast:  # found the cycle
                break
        return slow == 1  # see if the cycle is stuck on the number '1'


    
