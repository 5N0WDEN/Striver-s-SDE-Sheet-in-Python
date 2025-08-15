# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = -1, -1
        profit = 0
        for price in prices:
            if buy == -1:
                buy = price
            elif price < buy:
                buy = price
                sell = -1
            elif sell == -1 or (price > buy and price > sell):
                sell = price
                profit = max(profit, (sell - buy))
        return profit
