"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """最多只允许完成一笔交易"""
        _max = 0

        for i in range(len(prices) - 1):
            _max = max(_max, max(prices[i + 1:]) - prices[i])

        return _max

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        buying_prices = prices.copy()
        selling_prices = prices.copy()

        # 计算每一天的最优买入价
        buying_price = prices[0]
        for i in range(n):
            if prices[i] < buying_price:
                buying_price = prices[i]
            buying_prices[i] = buying_price

        # 计算每一天可操作的最高卖出价
        selling_price = prices[n - 1]
        for i in range(n - 1, -1, -1):
            if prices[i] > selling_price:
                selling_price = prices[i]
            selling_prices[i] = selling_price

        max_profit = max([y - x for x, y in zip(buying_prices, selling_prices)])

        return max(max_profit, 0)

    def maxProfit3(self, prices: List[int]) -> int:
        """dp[i] = max(dp[i-1], prices[i]+min(prices[:i))"""
        if len(prices) < 2:
            return 0
        _min = prices[0]
        res = 0
        for i in range(len(prices)):
            if prices[i] < _min:
                _min = prices[i]
            else:
                res = max(prices[i] - _min, res)

        return res


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
print(s.maxProfit3([7, 1, 5, 3, 6, 4]))
