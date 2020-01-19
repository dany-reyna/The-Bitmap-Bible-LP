from lib.graph import TreeNode


def inc_hash(hash_table, key, delta):
    new_count = hash_table.get(key, 0) + delta
    if new_count == 0:
        hash_table.pop(key)
    else:
        hash_table[key] = new_count


def count_paths(root, target, running, path_count):
    if root is None:
        return 0

    running += root.data

    paths = path_count.get(running - target, 0)
    if running == target:
        paths += 1

    inc_hash(path_count, running, 1)
    paths += count_paths(root.left, target, running, path_count)
    paths += count_paths(root.right, target, running, path_count)
    inc_hash(path_count, running, -1)

    return paths


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

    print(count_paths(my_root, 8, 0, dict()))
