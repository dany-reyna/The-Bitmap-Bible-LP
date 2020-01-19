from lib.graph import create_min_tree


def check_bst(root, min, max):
    if root is None:
        return True

    if (min is not None and root.data <= min) or (max is not None and root.data > max):
        return False

    if not check_bst(root.left, min, root.data) or not check_bst(root.right, root.data, max):
        return False

    return True


if __name__ == '__main__':
    root1 = create_min_tree([i for i in range(1, 5)])
    root1.left.data = 2
    print(check_bst(root1, None, None))

    root2 = create_min_tree([i for i in range(1, 5)])
    root2.right.data = 2
    print(check_bst(root2, None, None))
