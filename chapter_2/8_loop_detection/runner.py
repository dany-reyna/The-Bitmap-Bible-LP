from lib.list import create_list, get_n


def find_beginning(head):
    base = head
    runner = head

    while runner is not None and runner.next is not None:
        base = base.next
        runner = runner.next.next
        if base == runner:
            break

    if runner is None or runner.next is None:
        return None

    base = head
    while base != runner:
        base = base.next
        runner = runner.next

    return base


if __name__ == '__main__':
    head = create_list(11)
    print(f'List: {head}')

    fourth_node = get_n(head, 3)
    head.append_node_to_tail(fourth_node)

    print(f'Loop start: {find_beginning(head).data}')
