from lib.list import create_list


class Index:
    def __init__(self):
        self.value = 0


def kth_to_last(head, k, index):
    if head is None:
        return None
    node = kth_to_last(head.next, k, index)

    index.value += 1
    if index.value == k:
        return head

    return node


if __name__ == '__main__':
    head = create_list(5)
    k = 3
    index = Index()

    print(head)
    print('---')
    print(kth_to_last(head, k, index).data)
