from lib.errors import StackEmptyError
from lib.stack import StackWithCapacity


class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def get_last_stack(self):
        return self.stacks[-1] if len(self.stacks) > 0 else None

    def push(self, value):
        last = self.get_last_stack()
        if last is not None and not last.is_full():
            last.push(value)
        else:
            stack = StackWithCapacity(self.capacity)
            stack.push(value)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            raise StackEmptyError
        popped = last.pop()
        if len(last) == 0:
            self.stacks.pop()
        return popped


if __name__ == '__main__':
    stack = SetOfStacks(3)
    print(stack.get_last_stack())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.get_last_stack())
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.get_last_stack())
    stack.push(7)
    print(stack.get_last_stack())
    stack.pop()
    print(stack.get_last_stack())
    stack.pop()
    print(stack.get_last_stack())
    stack.pop()
    stack.pop()
    print(stack.get_last_stack())
