from lib.graph import create_min_tree


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def go_up(node, delta):
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1
    return node


def common_ancestor(n1, n2):
    delta = get_depth(n1) - get_depth(n2)
    if delta < 0:
        shallower = n1
        deeper = n2
        deeper = go_up(deeper, abs(delta))
    elif delta > 0:
        shallower = n2
        deeper = n1
        deeper = go_up(deeper, abs(delta))
    else:
        shallower = n1
        deeper = n2

    while shallower != deeper and shallower is not None and deeper is not None:
        shallower = shallower.parent
        deeper = deeper.parent

    return None if None in (shallower, deeper) else shallower


if __name__ == '__main__':
    root = create_min_tree([i for i in range(1, 10)])
    p = root.left.left
    q = root.left.right.right
    print(common_ancestor(p, q))
