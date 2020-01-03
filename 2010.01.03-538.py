"""
https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
538. 把二叉搜索树转换为累加树

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
"""
from tree import TreeNode, BinarySearchTree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """中序遍历再累加"""

        if not root:
            return root

        tree = []

        def inOrder(node):
            if node:
                inOrder(node.left)
                tree.append(node)
                inOrder(node.right)

        inOrder(root)
        tmp = 0
        for i in tree[::-1]:
            i.val, tmp = i.val + tmp, tmp + i.val

        for i in tree:
            if i.left == root.left and i.right == root.right:
                return i

    def convertBST2(self, root: TreeNode) -> TreeNode:
        """右中左"""
        self.sum = 0

        def inOrder(node):
            if node:
                inOrder(node.right)
                node.val += self.sum
                self.sum = node.val
                inOrder(node.left)

        inOrder(root)
        return root

    def convertBST3(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        accumulate_sum = 0

        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                pop_node = stack.pop()
                pop_node.val += accumulate_sum
                accumulate_sum = pop_node.val
                cur = pop_node.left
        return root


s = Solution()
convert = [s.convertBST, s.convertBST2, s.convertBST3]
for c in convert:
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(2)
    bst.insert(13)
    res = c(bst.root)
    print(TreeNode.levelOrder(res))
