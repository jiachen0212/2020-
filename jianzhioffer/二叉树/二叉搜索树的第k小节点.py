#coding=utf-8
# 二叉搜索树：左节点--根节点--右节点  依次增大   左父右 正好也是中序遍历
# 给定一棵二叉搜索树，请找出其中的第k小的结点。

# 递归实现
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k <= 0:
            return None
        res = []
        self.inOrder(pRoot, res)   # 从小到大
        if len(res) < k:
            return None
        return res[k - 1]

    def inOrder(self, root, res):
        if not root:
            return
        if root.left:  # 遍历左树
            self.inOrder(root.left, res)
        res.append(root)  # 添加父节点
        if root.right:    # 遍历右树
            self.inOrder(root.right, res)