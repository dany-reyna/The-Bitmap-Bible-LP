from lib.graph import create_min_tree


def leftmost_child(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root


def in_oder_successor(root):
    if root is None:
        return None

    if root.right is not None:
        return leftmost_child(root.right)
    else:
        s = root
        t = root.parent
        while t is not None and t.right == s:
            s = t
            t = t.parent
        return t


if __name__ == '__main__':
    root = create_min_tree([i for i in range(1, 10)])
    print(root)
    node = root.left.left
    s = in_oder_successor(node)
    print(s)
