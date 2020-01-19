class MyQueue:
    def __init__(self):
        self.stack_newest = []
        self.stack_oldest = []

    def add(self, value):
        self.stack_newest.append(value)

    def shift_stacks(self):
        if not self.stack_oldest:
            while self.stack_newest:
                self.stack_oldest.append(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest[-1]

    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    def __len__(self):
        return len(self.stack_newest) + len(self.stack_oldest)


if __name__ == '__main__':
    queue = MyQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue.stack_oldest)
    print(queue.stack_newest)
    print(queue.peek())
    print(queue.remove())
    print(queue.stack_oldest)
    print(queue.stack_newest)
