from lib.graph import create_min_tree


def is_covered(sub_root, node):
    if sub_root is None:
        return False
    if sub_root == node:
        return True
    return is_covered(sub_root.left, node) or is_covered(sub_root.right, node)


def ancestor_recursion(root, n1, n2):
    if root is None or root == n1 or root == n2:
        return root

    n1_on_left = is_covered(root.left, n1)
    n2_on_left = is_covered(root.left, n2)
    if n1_on_left != n2_on_left:
        return root

    children_side = root.left if n1_on_left else root.right
    return ancestor_recursion(children_side, n1, n2)


def common_ancestor(root, n1, n2):
    if not is_covered(root, n1) or not is_covered(root, n2):
        return None

    return ancestor_recursion(root, n1, n2)


if __name__ == '__main__':
    my_root = create_min_tree([i for i in range(1, 10)])
    p = my_root.left.left
    q = my_root.left.right.right
    print(common_ancestor(my_root, p, q))
