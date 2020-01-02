"""
https://leetcode-cn.com/problems/diameter-of-binary-tree/
543. 二叉树的直径

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
"""
from tree import Tree, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        对每个结点，计算左子树高度 + 右子树高度 + 1
        后序遍历
        """
        self.result = 1

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            length = left + right + 1
            self.result = max(self.result, length)
            return max(left, right) + 1

        dfs(root)

        return self.result - 1


s = Solution()
t = Tree()
t.create([1, 2, 3, 4, 5])
print(s.diameterOfBinaryTree(t.root))
