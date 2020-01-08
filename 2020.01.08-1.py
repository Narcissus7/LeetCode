"""
https://leetcode-cn.com/problems/two-sum/
1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """暴力"""
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """字典实现O(1)查找"""
        d = {num: str(i) for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target - num in d and int(d[target - num]) != i:
                return [i, int(d[target - num])]

        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """更优化的写法"""
        num_dict = {}
        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], index]
            else:
                num_dict[num] = index
        return []


s = Solution()
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum1([3, 2, 4], 6))
print(s.twoSum2([3, 2, 4], 6))
