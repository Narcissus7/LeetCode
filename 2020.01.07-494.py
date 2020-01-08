"""
494. 目标和
https://leetcode-cn.com/problems/target-sum/

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，
你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:
输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:
数组非空，且长度不会超过20。
初始的数组的和不会超过1000。
保证返回的最终结果能被32位整数存下。
"""
from typing import List
import collections


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        递归 超时了
        """
        self.count = 0

        def help(nums_, sum_):
            if not nums_:
                if sum_ == S:
                    self.count += 1
            else:
                help(nums_[1:], sum_ + nums_[0])
                help(nums_[1:], sum_ - nums_[0])

        help(nums, 0)

        return self.count

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        """
        动态规划
        dp[i][j]是从最开始的位置到第i个位置上能够成和为j的组合有多少种
        """
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[n][S]

    def findTargetSumWays3(self, nums: List[int], S: int) -> int:
        """
        转换成01背包问题
        找到nums一个正子集P和一个负子集N，使得总和等于target，统计这种可能性的总数
        https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/
        假如给定nums = [num1,num2,num3]，我们现在可以理解dp[j] = dp[j-num1] + dp[j-num2] + dp[j-num3]。
        """
        total = sum(nums)
        if (total + S) % 2 != 0 or total < S:
            return 0
        P = (total + S) // 2
        # dp的第x项，代表组合成数字x有多少方法
        dp = [1] + [0 for _ in range(P)]
        # 对每一个在nums数组中的数num而言，dp在从num到P的这些区间里，都可以加上一个num，来到达想要达成的P
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        print(dp)
        return dp[P]

    def findTargetSumWays4(self, nums: List[int], S: int) -> int:
        """
        动态规划
        dp[(i, j)]元祖第一位是目前的位数，第二位是目前的和
        """
        length, dp = len(nums), {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)


s = Solution()
# print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
# print(s.findTargetSumWays2([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays3([1, 2, 3, 4, 5], 3))
# print(s.findTargetSumWays([27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0], 10))
# print(s.findTargetSumWays2([27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0], 10))
# print(s.findTargetSumWays3([27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0], 10))

