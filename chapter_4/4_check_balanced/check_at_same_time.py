from graph import create_min_tree, TreeNode


def check_height(root):
    if root is None:
        return -1

    left_height = check_height(root.left)
    if left_height == float('-inf'):
        return float('-inf')

    right_height = check_height(root.right)
    if right_height == float('-inf'):
        return float('-inf')

    diff = abs(left_height - right_height)
    if diff > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    return check_height(root) != float('-inf')


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
