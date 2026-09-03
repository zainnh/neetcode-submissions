class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maximum = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                currentProf = prices[sell] - prices[buy]
                maximum = max(maximum, currentProf)
            else:
                buy = sell
            sell += 1
        return maximum
        