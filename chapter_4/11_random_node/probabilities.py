import random


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = None
        self.right = None

    def get_random_node(self):
        left_size = 0 if self.left is None else self.left.size
        index = random.randrange(self.size)

        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        elif index > left_size:
            return self.right.get_random_node()

    def insert_in_order(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert_in_order(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert_in_order(data)
        self.size += 1

    def find(self, data):
        if self.data == data:
            return self
        elif data <= self.data:
            return self.left.find(data) if self.left is not None else None
        elif data > self.data:
            return self.right.find(data) if self.right is not None else None
        return None

    def __repr__(self):
        string = f'{str(self.data)}<'
        if self.left is not None:
            string = f'{string}L: {str(self.left)}'
        if self.right is not None:
            string = f'{string}R: {str(self.right)}'
        string = f'{string}>'
        return string


if __name__ == '__main__':
    root = TreeNode(20)
    root.insert_in_order(10)
    root.insert_in_order(30)
    root.insert_in_order(5)
    root.insert_in_order(15)
    root.insert_in_order(3)
    root.insert_in_order(7)
    root.insert_in_order(17)

    print(root)

    print(root.get_random_node())
