from lib.graph import create_min_tree


class Result:
    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor

    def __repr__(self):
        return f'{repr(self.node)}, {self.is_ancestor}'


def ancestor_recursion(root, n1, n2):
    if root is None:
        return Result(None, False)
    if root == n1 and root == n2:
        return Result(root, True)

    left = ancestor_recursion(root.left, n1, n2)
    if left.is_ancestor:
        return left

    right = ancestor_recursion(root.right, n1, n2)
    if right.is_ancestor:
        return right

    if left.node is not None and right.node is not None:
        return Result(root, True)
    elif root == n1 or root == n2:
        is_ancestor = left.node is not None or right.node is not None
        return Result(root, is_ancestor)
    else:
        node = left.node if left.node is not None else right.node
        return Result(node, False)


def common_ancestor(root, n1, n2):
    result = ancestor_recursion(root, n1, n2)
    if result.is_ancestor:
        return result.node
    return None


if __name__ == '__main__':
    my_root = create_min_tree([i for i in range(1, 10)])
    p = my_root.left.left
    q = my_root.right.right.right
    print(common_ancestor(my_root, p, q))
