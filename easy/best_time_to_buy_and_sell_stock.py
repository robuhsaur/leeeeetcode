class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # array prices
        # prices[i] is the price of stock on the [ith] day

        profit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            profit = max(profit, price - buy)
        return profit
    
    # I DID IT!
    # used max() to update the profit variable
    # passed in the current value of profit & the price - buy