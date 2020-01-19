from lib.stack import Stack


class StackWithMin2(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def get_min(self):
        if self.min_stack.is_empty():
            return float('inf')
        return self.min_stack.peek()

    def push(self, value):
        if value <= self.get_min():
            self.min_stack.push(value)
        super().push(value)

    def pop(self):
        popped = super().pop()
        if popped == self.get_min():
            self.min_stack.pop()
        return popped


if __name__ == '__main__':
    stack = StackWithMin2()
    stack.push(5)
    print(stack.min_stack.peek())
    stack.push(6)
    print(stack.min_stack.peek())
    stack.push(3)
    print(stack.min_stack.peek())
    stack.push(7)
    print(stack.min_stack.peek())
    stack.pop()
    print(stack.min_stack.peek())
    stack.pop()
    print(stack.min_stack.peek())
