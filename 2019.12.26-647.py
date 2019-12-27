"""
https://leetcode-cn.com/problems/palindromic-substrings/

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
示例 1:
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".

示例 2:
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
"""

class Solution:
    num = 0
    def countSubstrings(self, s):
        """
        :param s: str
        :return: int
        在从左到右遍历字符串的同时，以每个字符为中心，向两边扩展开来判断各种可能成为回文数的组合
        """
        for i in range(len(s)):
            self.count(s, i, i)  # 奇
            self.count(s, i, i+1)  # 偶
        return self.num

    def count(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            self.num += 1
            start -= 1
            end += 1

    def countSubstrings2(self, s):
        """
        暴力
        """
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count

    def countSubstrings3(self, s):
        """
        动态规划
        单个字符是回文；两个连续字符如果相等是回文；如果有3个以上的字符，需要两头相等并且去掉首尾之后依然是回文。
        """
        count = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j):
                dp[i][j] = s[i] == s[j] and (dp[i + 1][j - 1] or (j - i < 2))
                if dp[i][j]:
                    count += 1

            dp[j][j] = 1  # 自身是回文数
            count += 1
        return count
