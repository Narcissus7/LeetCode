"""
https://leetcode-cn.com/problems/continuous-subarray-sum/
523. 连续的子数组和
给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，
其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例 1:
输入: [23,2,4,6,7], k = 6    输出: True
解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2:
输入: [23,2,6,4,7], k = 6    输出: True
解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。

说明:
数组的长度不会超过10,000。
你可以认为所有数字总和在 32 位有符号整数范围内。
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """暴力"""
        for i in range(len(nums) - 1):
            for j in range(i + 2, len(nums) + 1):
                if k == 0:
                    if sum(nums[i:j]) == 0:
                        return True
                    else:
                        break

                if sum(nums[i:j]) // k == sum(nums[i:j]) / k:
                    return True

        return False

    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        """快一点的暴力，能过"""
        for i in range(len(nums) - 1):
            tmp = nums[i]
            for j in range(i + 1, len(nums)):
                tmp += nums[j]
                if k == 0:
                    if tmp == 0:
                        return True
                    else:
                        break

                if tmp // k == tmp / k:
                    return True

        return False

    def checkSubarraySum3(self, nums: List[int], k: int) -> bool:
        """
        使用 HashMap 来保存到第 i 个元素为止的累积和，但我们对这个前缀和除以 k 取余数
        假设:
            a[i]+a[i+1]+...+a[j]=n1k+q;
        如果存在一个n
            n>j且a[i]+a[i+1]+...+a[j]+...+a[n]=n2k+q;
        那么
            a[j+1]+...+a[n]=(n2−n1)k

        如果同一个余数出现了两次，并且两次出现的下标之差大于1，那么就表示在这两个坐标之间的元素之和是k的倍数
        只有当k不为0时才对当前的和求余
        对于nums = [0, 0], k = 0的情况，需要添加一个初始映射(0, -1)来确保结果的正确
        """
        if len(nums) < 2:
            return False
        bag = {0: -1}
        sums = 0  # 求和
        for i in range(len(nums)):
            sums += nums[i]
            if k != 0:
                sums = sums % k  # 取余: 位置i
            if sums not in bag:
                bag[sums] = i
            else:
                if i - bag.get(sums) > 1:
                    return True
        return False


s = Solution()
print(s.checkSubarraySum([0, 0], 0))
print(s.checkSubarraySum2([0, 0], 0))
print(s.checkSubarraySum3([2, 5, 33, 6, 7, 25, 15], 13))
