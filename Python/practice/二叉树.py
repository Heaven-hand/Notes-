import null as null


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = [3,4,5,1,3,null,1]
print(root.val)


def dp(self, root):
    if not root:
        return [0, 0]  # 列表[0]代表当前节点不偷带来的钱，列表[1]代表当前节点偷带来的钱
    l = self.dp(root.left)  # root的左节点[不偷][偷]带来的钱
    r = self.dp(root.right)  # root的右节点[不偷][偷]带来的钱
    # root节点不偷，则偷左右儿子节点，取左儿子偷或不偷的最大值和右儿子偷或不偷的最大值；
    # root节点偷，则root节点值+左儿子不偷+右儿子不偷。
    return [max(l) + max(r), root.val + l[0] + r[0]]


def rob(self, root: TreeNode) -> int:
    if not root:
        return 0
    return max(self.dp(root))  # 取root节点偷或不偷的最大值