from lib.graph import TreeNode


def recurse(array, start, end):
    if start > end:
        return None

    mid = int((start + end) / 2)
    n = TreeNode(array[mid])
    n.left = recurse(array, start, mid - 1)
    n.right = recurse(array, mid + 1, end)
    return n


def create_min_tree(array):
    return recurse(array, 0, len(array) - 1)


if __name__ == '__main__':
    root = create_min_tree([i for i in range(6)])
    print(root)
