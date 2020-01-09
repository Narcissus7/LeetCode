"""
713. 乘积小于K的子数组
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
说明:

0 < nums.length <= 50000
0 < nums[i] < 1000
0 <= k < 10^6
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """暴力"""
        count = 0
        for i in range(len(nums)):
            tmp = 1
            for j in range(i, len(nums)):
                tmp *= nums[j]
                if tmp < k:
                    count += 1
                else:
                    break
        return count

    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        """
        双指针
        1.如果当前窗口乘积小于k，记录当前窗口大小，右边界则向右滑动一格，
        2.如果乘积大于等于k，先将左边第一格的数除掉，左边窗口向右滑动一格。
        """
        if k <= 1:
            return 0
        left = count = 0
        mul = 1
        for i in range(len(nums)):
            mul *= nums[i]
            while mul >= k:
                mul /= nums[left]
                left += 1
            count += i - left + 1
        return count


s = Solution()
print(s.numSubarrayProductLessThanK2([10, 5, 2, 6], 100))
