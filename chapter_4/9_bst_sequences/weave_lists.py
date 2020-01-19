from collections import deque
from lib.graph import create_min_tree


def weave_lists(l1, l2, prefix, weaved):
    if not l1 or not l2:
        weaved.append(
            deque([*prefix, *l1, *l2])
        )
        return

    prefix.append(l1.popleft())
    weave_lists(l1, l2, prefix, weaved)
    l1.appendleft(prefix.pop())

    prefix.append(l2.popleft())
    weave_lists(l1, l2, prefix, weaved)
    l2.appendleft(prefix.pop())


def all_seqs(root):
    result = []

    if root is None:
        result.append([])
        return result

    prefix = [root.data]

    left_seqs = all_seqs(root.left)
    right_seqs = all_seqs(root.right)

    for left in left_seqs:
        for right in right_seqs:
            weaved = []
            weave_lists(left, right, prefix, weaved)
            result.extend(weaved)

    return result


if __name__ == '__main__':
    my_root = create_min_tree([i for i in range(1, 4)])
    sequences = all_seqs(my_root)
    for s in sequences:
        print(s)
