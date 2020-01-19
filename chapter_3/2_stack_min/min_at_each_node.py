from lib.stack import Stack


class StackWithMin(Stack):
    class NodeWithMin(Stack.StackNode):
        def __init__(self, data, minimum):
            super().__init__(data)
            self.min = minimum

    def get_min(self):
        if self.is_empty():
            return float('inf')
        return self.peek().min

    def push(self, value):
        new_min = min(value, self.get_min())
        super().push(self.NodeWithMin(value, new_min))


if __name__ == '__main__':
    stack = StackWithMin()
    stack.push(5)
    print(stack.peek().min)
    stack.push(6)
    print(stack.peek().min)
    stack.push(3)
    print(stack.peek().min)
    stack.push(7)
    print(stack.peek().min)
    stack.pop()
    print(stack.peek().min)
    stack.pop()
    print(stack.peek().min)
