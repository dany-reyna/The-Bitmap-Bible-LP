from lib.errors import StackEmptyError


class Node:
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0

    def is_full(self):
        return self.capacity == self.size

    @staticmethod
    def join(above, below):
        if below is not None:
            below.above = above
        if above is not None:
            above.below = below

    def push(self, value):
        if self.size >= self.capacity:
            return False
        self.size += 1
        node = Node(value)
        if self.size == 1:
            self.bottom = node
        self.join(node, self.top)
        self.top = node
        return True

    def pop(self):
        popped = self.top
        self.top = self.top.below
        self.size -= 1
        return popped.value

    def is_empty(self):
        return self.size == 0

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom is None:
            self.bottom.below = None
        self.size += 1
        return b.value


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        return self.stacks[-1] if len(self.stacks) > 0 else None

    def push(self, value):
        last = self.get_last_stack()
        if last is not None and not last.is_full():
            last.push(value)
        else:
            stack = Stack(self.capacity)
            stack.push(value)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            raise StackEmptyError
        popped = last.pop()
        if last.size == 0:
            self.stacks.pop()
        return popped

    def is_empty(self):
        last = self.get_last_stack()
        return last is None or last.is_empty()

    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        if remove_top:
            popped = stack.pop()
        else:
            popped = stack.remove_bottom()

        if stack.is_empty():
            del self.stacks[index]
        elif index + 1 < len(self.stacks):
            value = self.left_shift(index + 1, False)
            stack.push(value)
        return popped

    def pop_at(self, index):
        return self.left_shift(index, True)


if __name__ == '__main__':
    stacks = SetOfStacks(5)
    for i in range(34):
        stacks.push(i)
    for i in range(34):
        print(f'Popped: {stacks.pop()}')
