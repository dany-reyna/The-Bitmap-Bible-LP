from lib.graph import create_min_tree

last_visited = None


def check_bst(root):
    global last_visited

    if root is None:
        return True

    if not check_bst(root.left):
        return False

    if last_visited is not None and last_visited.data > root.data:
        return False
    last_visited = root

    if not check_bst(root.right):
        return False

    return True


if __name__ == '__main__':
    root1 = create_min_tree([i for i in range(1, 5)])
    root1.left.data = 2
    print(check_bst(root1))

    root2 = create_min_tree([i for i in range(1, 5)])
    root2.right.data = 2
    print(check_bst(root2))
