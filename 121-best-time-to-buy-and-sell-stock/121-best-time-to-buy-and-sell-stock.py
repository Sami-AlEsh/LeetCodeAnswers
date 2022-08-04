class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 1e5
        sell = -1
        ans = 0
        
        for num in prices:
            if num < buy:
                buy = num
                sell = -1
            
            elif num > sell:
                sell = num
                if sell - buy > ans:
                    ans = sell - buy
        
        return ans