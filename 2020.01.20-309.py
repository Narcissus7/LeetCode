"""
309. 最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        """

        sold = 0  # 卖出
        rest = 0  # 休息
        hold = -float('inf')  # 持有

        for price in prices:
            sold, hold, rest = hold + price, max(hold, rest - price), max(rest, sold)

        return max(sold, rest)

    def maxProfit2(self, prices: List[int]) -> int:
        """
        dp1: 当天未持股的最大利润
        dp2: 当天持股的最大利润
        """
        n = len(prices)
        if n < 2:
            return 0

        if n == 2:
            return max(0, prices[1]-prices[0])

        dp1 = [0] * n
        dp2 = [0] * n
        dp2[0] = -prices[0]  # 若第1天持股此时利润为-prices[0]

        for i in range(1, n):
            dp1[i] = max(dp1[i-1], dp2[i-1] + prices[i])
            dp2[i] = max(dp2[i - 1], dp1[i - 2] - prices[i])  # 若前天未持有股票的话，则今天一定不再冷冻期,可以持股（买入）

        return max(dp1[-1], dp2[-1])

    def maxProfit3(self, prices: List[int]) -> int:
        """
        优化
        """
        n = len(prices)
        if n < 2:
            return 0

        if n == 2:
            return max(0, prices[1]-prices[0])

        dp1 = [0] * n
        dp2 = [0] * n
        dp2[0] = -prices[0]  # 若第1天持股此时利润为-prices[0]

        for i in range(1, n):
            dp1[i] = max(dp1[i-1], dp2[i-1] + prices[i])
            dp2[i] = max(dp2[i - 1], dp1[i - 2] - prices[i])  # 若前天未持有股票的话，则今天一定不再冷冻期,可以持股（买入）

        return max(dp1[-1], dp2[-1])

s = Solution()
print(s.maxProfit([1, 2, 3, 0, 2]))
print(s.maxProfit2([1, 2, 3, 0, 2]))
print(s.maxProfit([1, 4]))
print(s.maxProfit2([1, 4]))
