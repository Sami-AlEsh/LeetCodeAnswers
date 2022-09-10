class Solution:
    def arrangeCoins(self, n: int) -> int:
        return(int(floor(0.5*(-1+sqrt(1+8*n))))) 
