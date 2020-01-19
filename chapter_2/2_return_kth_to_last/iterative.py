from lib.list import create_list


def kth_to_last(head, k):
    base = head
    runner = head

    for _ in range(k):
        if runner is None:
            return runner
        runner = runner.next

    while runner is not None:
        base = base.next
        runner = runner.next
    return base


if __name__ == '__main__':
    head = create_list(5)
    k = 3
    print(head)
    print('---')
    print(kth_to_last(head, k).data)
