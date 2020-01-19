from lib.graph import create_min_tree


def get_sibling(node):
    if None in (node, node.parent):
        return None

    parent = node.parent
    return parent.right if parent.left == node else parent.left


def is_covered(sub_root, node):
    if sub_root is None:
        return False
    if sub_root == node:
        return True
    return is_covered(sub_root.left, node) or is_covered(sub_root.right, node)


def common_ancestor(root, n1, n2):
    if not is_covered(root, n1) or not is_covered(root, n2):
        return None
    elif is_covered(n1, n2):
        return n1
    elif is_covered(n2, n1):
        return n2

    sibling = get_sibling(n1)
    parent = n1.parent
    while not is_covered(sibling, n2):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent


if __name__ == '__main__':
    root = create_min_tree([i for i in range(1, 10)])
    p = root.left.left
    q = root.left.right.right
    print(common_ancestor(root, p, q))
