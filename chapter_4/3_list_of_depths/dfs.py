from lib.graph import create_min_tree


def create_levels_list(root, lists, level):
    if root is None:
        return

    if len(lists) == level:
        _list = []
        lists.append(_list)
    else:
        _list = lists[level]

    _list.append(root.data)
    create_levels_list(root.left, lists, level + 1)
    create_levels_list(root.right, lists, level + 1)


if __name__ == '__main__':
    my_root = create_min_tree([i for i in range(6)])
    print(my_root)
    my_lists = []
    create_levels_list(my_root, my_lists, 0)
    print(my_lists)
