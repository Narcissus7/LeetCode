from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def levelOrder(root):
        if not root:
            return None
        q = [root]
        res = []
        while q:
            node = q.pop(0)
            res.append(node.val)
            if node.left:
                q.append(node.left)
                if not node.right:
                    q.append(TreeNode(None))
            if node.right:
                if not node.left:
                    q.append(TreeNode(None))
                q.append(node.right)
        return res


class Tree:
    def __init__(self):
        self.root = None

    def create(self, value_list):
        if not value_list:
            return None
        self.root = TreeNode(value_list[0])
        queue = deque([self.root])
        nums = 1
        while nums < len(value_list):
            node = queue.popleft()
            if node:
                node.left = TreeNode(value_list[nums]) if value_list[nums] else None
                queue.append(node.left)
            if nums + 1 < len(value_list):
                node.right = TreeNode(value_list[nums + 1]) if value_list[nums + 1] else None
                queue.append(node.right)
                nums += 1
            nums += 1

    # 前序遍历，中左右
    def preOrder(self):
        self._preOrder(self.root)

    def _preOrder(self, node):
        if node:
            print(node.val)
            self._preOrder(node.left)
            self._preOrder(node.right)

    # 中序遍历，左中右
    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node:
            self._inOrder(node.left)
            print(node.val)
            self._inOrder(node.right)

    # 后序遍历，左右中
    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.val)

    # 层序遍历，广度优先遍历  用队列实现
    def levelOrder(self):
        if not self.root:
            return []
        q = [self.root]
        while q:
            node = q.pop(0)
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)