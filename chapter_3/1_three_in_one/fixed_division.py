from lib.errors import StackFullError, StackEmptyError


class FixedMultiStack:
    def __init__(self, stack_size):
        self.n_stacks = 3
        self.stack_size = stack_size
        self.values = [None] * (self.n_stacks * self.stack_size)
        self.sizes = [0] * self.n_stacks

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def top_index(self, stack_num):
        offset = self.stack_size * stack_num
        return offset + self.sizes[stack_num] - 1

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise StackFullError(stack_num)
        self.sizes[stack_num] += 1
        self.values[self.top_index(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise StackEmptyError(stack_num)
        top = self.top_index(stack_num)
        popped = self.values[top]
        self.values[top] = None
        self.sizes[stack_num] -= 1
        return popped

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise StackEmptyError(stack_num)
        return self.values[self.top_index(stack_num)]
