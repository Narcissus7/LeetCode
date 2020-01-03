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
        """
        又是动态规划
        dp[i]表示字符串s[:i]能否拆分成符合要求的子字符串
        """
        len_dic = len(wordDict)
        len_str = len(s)
        dp = [0] * len_str
        for i in range(len_str):
            for j in range(len_dic):
                len_j = len(wordDict[j])
                if i + 1 >= len_j and wordDict[j] == s[i + 1 - len_j:i + 1] and (
                        i + 1 - len_j == 0 or dp[i - len_j] == 1):
                    dp[i] = 1
                    break
        return dp[len_str - 1] == 1

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        starts = [0]
        wordDict = set(wordDict)
        for i in range(1, N + 1):
            for index in starts:
                if s[index:i] in wordDict:
                    starts.append(i)
                    break
        return starts[-1] == N

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

    def wordBreak4(self, s: str, wordDict: List[str]) -> bool:
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

s = "cars"
wordDict = ["car", "ca", "rs"]

# s = "bb"
# wordDict = ["a", "b", "bbb", "bbbb"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

slt = Solution()
print(slt.wordBreak(s, wordDict))
print(slt.wordBreak2(s, wordDict))
