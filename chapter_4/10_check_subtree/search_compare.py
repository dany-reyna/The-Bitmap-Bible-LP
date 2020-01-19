from lib.graph import TreeNode


def compare(n1, n2):
    if n1 is None and n2 is None:
        return True
    elif None in (n1, n2):
        return False
    elif n1.data != n2.data:
        return False
    return compare(n1.left, n2.left) and compare(n1.right, n2.right)


def search(n1, n2):
    if n1 is None:
        return False
    elif n1.data == n2.data and compare(n1, n2):
        return True

    return search(n1.left, n2) or search(n1.right, n2)


def contains_tree(n1, n2):
    if n2 is None:
        return True
    return search(n1, n2)


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)

    root2 = TreeNode(2)
    root2.left = TreeNode(4)

    print(contains_tree(root1, root2))
