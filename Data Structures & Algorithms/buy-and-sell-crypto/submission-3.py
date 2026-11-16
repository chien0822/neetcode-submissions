class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                now=0
                if prices[i]< prices[j]:
                    now = prices[j]-prices[i]
                    profit=max(now,profit)
        return profit
        