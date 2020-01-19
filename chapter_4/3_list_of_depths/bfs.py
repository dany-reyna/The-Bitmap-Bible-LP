from collections import deque
from lib.graph import create_min_tree


def create_levels_list(root):
    lists = []

    queue = deque()
    if root is not None:
        queue.append(root)

    while queue:
        lists.append([n.data for n in queue])
        parents = queue
        queue = deque()
        for node in parents:
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return lists


if __name__ == '__main__':
    my_root = create_min_tree([i for i in range(7)])
    print(my_root)
    lists = create_levels_list(my_root)
    print(lists)
