"""
152. 乘积最大子序列

给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        mul_max = nums[0]

        for i, num in enumerate(nums):
            tmp = 1
            for j in range(i, len(nums)):
                tmp *= nums[j]
                if tmp > mul_max:
                    mul_max = tmp

        return mul_max

    def maxProduct2(self, nums: List[int]) -> int:
        """
        由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值cur_min
        """
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min

        return res

    def maxProduct3(self, nums: List[int]) -> int:
        """
        当负数个数为偶数时候, 全部相乘一定最大
        当负数个数为奇数时候, 它的左右两边的负数个数一定为偶数, 只需求两边最大值
        当有0情况,重置就可以了
        """
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1  # nums[i - 1]为0时*1
            reverse_nums[i] *= reverse_nums[i - 1] or 1

        return max(nums + reverse_nums)


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct2([2, 3, -2, 4]))
print(s.maxProduct3([2, 3, -2, 4]))
