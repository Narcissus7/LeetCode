"""
https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
581. 最短无序连续子数组
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :param nums: List[int]
        :return: int
        对比排序后数组, 找出首位第一个不同的数字，中间即是最短无序连续子数组
        """
        sorted_nums = sorted(nums)
        if sorted_nums == nums:  # 排序后数组与原数组相等为0
            return 0
        start = 0
        end = 0
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                start = i
                break
        for i in range(len(nums)-1, -1, -1):
            if sorted_nums[i] != nums[i]:
                end = i
                break

        return end - start + 1

    def findUnsortedSubarray2(self, nums):
        """
        :param nums: List[int]
        :return: int
        两次遍历：从前往后找右边界、从后往前找左边界
        从前往后: right=0, max = nums[0]
                 if (nums[i] >= max):
                    max = nums[i]
                else:
                    right = i
        从后往前: 同理
        """
        start = len(nums) - 1
        end = 0
        max_num = nums[0]
        min_num = nums[-1]
        for i in range(len(nums)):
            if nums[i] >= max_num:
                max_num = nums[i]
            else:
                end = i
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= min_num:
                min_num = nums[i]
            else:
                start = i

        return end - start + 1 if end > start else 0

    def findUnsortedSubarray3(self, nums):
        """
        :param nums: List[int]
        :return: int
        单调栈（题739）
        """
        left = len(nums) - 1
        right = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[j]:
                right = max(right, stack.pop())
            stack.append(j)

        return right - left + 1 if right > left else 0


s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray2([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray3([2, 6, 4, 8, 10, 9, 15]))