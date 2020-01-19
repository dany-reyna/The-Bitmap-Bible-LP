from lib.graph import TreeNode


def count_from_node(node, target_sum, current_sum):
    if node is None:
        return 0

    current_sum += node.data

    paths = 0
    if current_sum == target_sum:
        paths += 1

    paths += count_from_node(node.left, target_sum, current_sum)
    paths += count_from_node(node.right, target_sum, current_sum)

    return paths


def count_paths(root, target_sum):
    if root is None:
        return 0

    paths_root = count_from_node(root, target_sum, 0)

    paths_left = count_paths(root.left, target_sum)
    paths_right = count_paths(root.right, target_sum)

    return paths_root + paths_left + paths_right


if __name__ == '__main__':
    my_root = TreeNode(10)
    my_root.left = TreeNode(5)
    my_root.right = TreeNode(-3)
    my_root.left.left = TreeNode(3)
    my_root.left.right = TreeNode(2)
    my_root.right.right = TreeNode(11)
    my_root.left.left.left = TreeNode(3)
    my_root.left.left.right = TreeNode(-2)
    my_root.left.right.right = TreeNode(1)

    print(count_paths(my_root, 8))
