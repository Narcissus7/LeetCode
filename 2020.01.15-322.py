"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
"""
from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def helper(n):
            if n in memo:
                return memo[n]
            res = float("inf")
            for coin in coins:
                if n >= coin:
                    res = min(res, helper(n - coin) + 1)
            memo[n] = res
            return res

        return helper(amount) if (helper(amount) != float("inf")) else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (i >= coin):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if (dp[-1] != float("inf")) else -1

    def coinChange3(self, coins: List[int], amount: int) -> int:
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for c in coins:  # 枚举硬币种数
            for j in range(c, amount + 1):  # 从小到大枚举金额，确保j-c >= 0.
                f[j] = min(f[j], f[j - c] + 1)
        return f[amount] if f[amount] != float('inf') else -1

    def coinChange4(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins = sorted(coins, reverse=True)
        res = amount + 1

        def dfs(index, target, count):
            nonlocal res
            this_coin = coins[index]
            if count + math.ceil(target / this_coin) >= res:
                return

            if target % this_coin == 0:
                res = count + target // this_coin

            if index == n - 1:
                return

            for i in range(target // this_coin, -1, -1):
                dfs(index + 1, target - i * this_coin, count + i)

        dfs(0, amount, 0)
        return -1 if res == amount + 1 else res


s = Solution()
print(s.coinChange([7, 5, 3, 2], 18))
print(s.coinChange2([7, 5, 3, 2], 18))
print(s.coinChange3([7, 5, 3, 2], 18))
print(s.coinChange4([7, 5, 3, 2], 18))
