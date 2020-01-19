from lib.graph import TreeNode


def get_order_list(node, lst):
    if node is None:
        lst.append("None")
        return

    lst.append(node.data)
    get_order_list(node.left, lst)
    get_order_list(node.right, lst)


def contains_tree(n1, n2):
    l1 = []
    l2 = []

    get_order_list(n1, l1)
    get_order_list(n2, l2)

    return ''.join([str(i) for i in l2]) in ''.join([str(i) for i in l1])


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)

    root2 = TreeNode(2)
    root2.left = TreeNode(4)

    print(contains_tree(root1, root2))
