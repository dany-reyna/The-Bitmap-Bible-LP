from lib.graph import create_min_tree, TreeNode


def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root):
    if root is None:
        return True

    diff = abs(get_height(root.left) - get_height(root.right))
    if diff > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


if __name__ == '__main__':
    my_root = create_min_tree([i for i in range(6)])
    print(my_root)
    print(is_balanced(my_root))

    my_root = TreeNode(0)
    node = my_root
    for i in range(1, 5):
        node.left = TreeNode(i)
        node = node.left
    print(my_root)
    print(is_balanced(my_root))
