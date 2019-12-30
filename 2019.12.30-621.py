"""
https://leetcode-cn.com/problems/task-scheduler/

给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，
并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
"""
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        """
        公式 max = (most - 1) * (n + 1) + num_most
        贪心？
        :param tasks:
        :param n:
        :return: int
        """
        count = Counter(tasks)
        most = count.most_common()[0][1]
        num_most = len([i for i, v in count.items() if v == most])
        time = (most - 1) * (n + 1) + num_most
        return max(time, len(tasks))

    def leastInterval2(self, tasks, n):
        """
        优先级队列 ?
        """
        ts = [0] * 26
        for t in tasks:
            ts[ord(t) - ord('A')] += 1

        q = [t for t in ts if t != 0]
        res = 0
        while q:
            # print(q)
            for i in range(n + 1):
                if i < len(q):
                    q[i] -= 1

                res += 1
                if not any(q):
                    break

            q = sorted([i for i in q if i != 0], reverse=True)
        return res

    def leastInterval3(self, tasks, n):
        """
        优先级队列按照元素出现次数进行排序。
        while(队列不为空)
            每次从队列中取出 n + 1 个元素
            将每个元素次数减一，如果不为 0，则再次放入队列
            如果队列不为空，则说明前一次完整取出 n + 1 个元素，将结果加到 res，否则取实际取出元素个数 cnt 加到 res。
        """
        ts = [0] * 26
        for t in tasks:
            ts[ord(t) - ord('A')] += 1

        q = [t for t in ts if t != 0]
        res = 0
        while q:
            for i in range(n + 1):
                if i < len(q):
                    q[i] -= 1

            if any(q):
                res += n + 1
            else:
                res += len(q)

            q = sorted([i for i in q if i != 0], reverse=True)
        return res


s = Solution()
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"], n=2))
print(s.leastInterval2(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"], n=2))
print(s.leastInterval3(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"], n=2))
