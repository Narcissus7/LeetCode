"""
https://leetcode-cn.com/problems/word-break/
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        starts = [0]
        wordDict = set(wordDict)  # 将查找时间变为常数级
        for i in range(1, N + 1):
            for index in starts:
                if s[index:i] in wordDict:
                    starts.append(i)
                    break
        return starts[-1] == N

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """
        和上一个思路一样
        子数组或者子字符串且求极值的题，基本就是 DP 没差
        dp[i]表示字符串s[:i]能否拆分成符合要求的子字符串
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        """上一个的递归版本"""
        wordDict = set(wordDict)
        import functools
        @functools.lru_cache(None)  # 递归可以缓存已返回的结果
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)

s = "applepenapple"
wordDict = ["apple", "pen"]

# s = "cars"
# wordDict = ["car", "ca", "rs"]

# s = "bb"
# wordDict = ["a", "b", "bbb", "bbbb"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

slt = Solution()
print(slt.wordBreak(s, wordDict))
print(slt.wordBreak2(s, wordDict))
print(slt.wordBreak3(s, wordDict))
