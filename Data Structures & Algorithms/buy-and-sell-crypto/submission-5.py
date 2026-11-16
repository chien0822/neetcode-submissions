class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for sell in range(len(prices)-1,0,-1):
                now=0
                buy = min(prices[:sell])
                if buy< prices[sell]:
                    now = prices[sell] - buy
                profit=max(now,profit)
        return profit