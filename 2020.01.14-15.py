"""
15. 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                tmp = nums[:i] + nums[i + 1:j] + nums[j + 1:]
                if -(nums[i] + nums[j]) in tmp:
                    res.append([nums[i], nums[j], -(nums[i] + nums[j])])

        d = {str(sorted(i)): sorted(i) for i in res}
        return list(d.values())

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        left, right = 0, len(nums) - 1
        res = {}

        def help(i, j):
            if i >= j:
                return
            tmp = -(nums[i] + nums[j])
            if tmp in nums[i + 1:j]:
                res[str(sorted([nums[i], nums[j], tmp]))] = (nums[i], nums[j], tmp)
            help(i, j - 1)
            help(i + 1, j)

        help(left, right)

        return list(res.values())

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        # 从小到大排序
        if len(nums) < 3:
            return []
        nums.sort()
        ans = set()

        for i, a in enumerate(nums[:-2]):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            hash_dict = {}
            for b in nums[i + 1:]:
                if b not in hash_dict:  # 把 c 加入哈希表
                    hash_dict[-(a + b)] = 1
                else:
                    ans.add((a, -(a + b), b))
        return list(ans)


s = Solution()
print(s.threeSum([-2, 0, 1, 1, 2]))
print(s.threeSum2([-2, 0, 1, 1, 2]))
print(s.threeSum3([-2, 0, 1, 1, 2]))