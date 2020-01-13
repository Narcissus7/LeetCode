"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划
        dp[i] = max(nums[i], dp[i-1]+nums[i])
        """
        dp = [i for i in nums]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])

        return max(dp)

    def maxSubArray2(self, nums: List[int]) -> int:
        """优化空间复杂度 贪心？"""
        max_num = nums[0]
        tmp = nums[0]

        for i in range(1, len(nums)):
            tmp = max(nums[i], tmp+nums[i])
            max_num = max(max_num, tmp)

        return max_num

    def maxSubArray3(self, nums: List[int]) -> int:
        """
        分治
        https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode/
        """
        return self.helper(nums, 0, len(nums) - 1)

    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
