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


# -------------- 二叉搜索树 -----------------
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._count = 0

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):  # 尝试非递归实现

        if root is None:
            self._count += 1
            return TreeNode(val)

        if val == root.val:
            root.val = val  # 插入的value已存在时要更新值
        elif val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        return root

    def contain(self, val):
        return self._contain(self.root, val)

    def _contain(self, node, val):
        if not node:
            return False

        if val == node.val:
            return True
        elif val < node.val:
            self._contain(node.left, val)
        else:
            self._contain(node.right, val)

    # 以node为根结点的二分搜索树中查找value， 若value不存在 返回null
    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return None
        if val == node.val:
            return node.val
        elif val > node.val:
            return self._search(node.right, val)
        else:
            return self._search(node.left, val)

    # ------------ 遍历 ----------------
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
        if self.isEmpty():
            return []
        q = [self.root]
        while q:
            node = q.pop(0)
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    # -------- 删除一个节点 ---------------
    # 删除最小值或最大值

    # 寻找最小值
    def minimum(self):
        if self.isEmpty():
            return None
        minNode = self._minimum(self.root)
        return minNode.val

    def _minimum(self, node):
        if node.left == None:
            return node
        return self._minimum(node.left)

    # 寻找最大值
    def maximum(self):
        if self.isEmpty():
            return None
        maxNode = self._maximum(self.root)
        return maxNode.val

    def _maximum(self, node):
        if node.right == None:
            return node
        return self._maximum(node.right)

    # 删除最小值
    def removeMin(self):
        if self.root:
            self.root = self._removeMin(self.root)

    # 返回删除节点后新的二分搜索树的根
    def _removeMin(self, node):
        if node.left == None:
            rightNode = node.right
            self._count -= 1
            return rightNode

        node.left = self._removeMin(node.left)
        return node

    # 删除最大值
    def removeMax(self):
        if self.root:
            self.root = self._removeMax(self.root)

    # 返回删除节点后新的二分搜索树的根
    def _removeMax(self, node):
        if node.right == None:
            leftNode = node.left
            self._count -= 1
            return leftNode

        node.right = self._removeMax(node.right)
        return node

    # 删除任意节点、右子树中的最小值代替删除节点、或左子树的最大值
    # 从二叉树中删除键值为value的节点
    def remove(self, val):
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._remove(node.left, val)
        elif val > node.val:
            node.right = self._remove(node.right, val)
        else:  # val == node.val
            if node.left == None:  # 左孩子为空
                rightNode = node.right
                self._count -= 1
                return rightNode
            elif node.right == None:  # 左孩子为空
                self._count -= 1
                return node.left
            else:  # 要删除节点的左右孩子均存在
                successor = self._minimum(node.rigth)  # 右子树中的最小节点  后继
                self._count += 1
                successor.right = self.removeMin(node.right)
                successor.left = node.left

                node.left = node.right = TreeNode
                self._count -= 1

                return successor