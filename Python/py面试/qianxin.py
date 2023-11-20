def steal(root: TreeNode):
    if root == None:
        return [0, 0]
    L = steal(root.left)
    R = steal(root.right)

    # 偷当前的节点
    yes = root.val + L[0] + R[0]
    # 不偷当前节点
    no = max(L[0], L[1]) + max(R[0], R[1])
    return [no, yes]


value = steal(root)
return max(value)
