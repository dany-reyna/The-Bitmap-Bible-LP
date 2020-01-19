from lib.errors import StackEmptyError, StackFullError


class StackInfo:
    def __init__(self, multi_stack, start, capacity):
        self.multi_stack = multi_stack
        self.start = start
        self.capacity = capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def last_capacity_index(self):
        return self.multi_stack.adjust_index(self.start + self.capacity - 1)

    def last_element_index(self):
        return self.multi_stack.adjust_index(self.start + self.size - 1)

    # Check if an index on the full array is within the stack boundaries.
    # The stack can wrap around to the start of the array.
    def is_within_capacity(self, index):
        # If outside of bounds of array, return false.
        if index < 0 or index >= len(self.multi_stack.values):
            return False

        #  If index wraps around, adjust it.
        contiguous_index = index + len(self.multi_stack.values) if index < self.start else index
        end = self.start + self.capacity
        return self.start <= contiguous_index < end


class MultiStack:
    def __init__(self, n_stacks, default_size):
        self.info = []
        for i in range(n_stacks):
            self.info.append(StackInfo(self, default_size * i, default_size))
        self.values = [None] * (n_stacks * default_size)

    def number_of_elements(self):
        size = 0
        for si in self.info:
            size += si.size
        return size

    def all_stacks_are_full(self):
        return self.number_of_elements() == len(self.values)

    # Adjust index to be within the range of 0 -> length - 1.
    def adjust_index(self, index):
        length = len(self.values)
        return ((index % length) + length) % length

    def previous_index(self, index):
        return self.adjust_index(index - 1)

    def next_index(self, index):
        return self.adjust_index(index + 1)

    def next_stack(self, stack_num):
        return (stack_num + 1) % len(self.info)

    def expand(self, stack_num):
        self.shift(self.next_stack(stack_num))
        self.info[stack_num].capacity += 1

    # Shift items in stack over by one element.
    # If we have available capacity, then we'll end up shrinking the stack by one element.
    # If we don't have available capacity, then we'll need to shift the next stack over too.
    def shift(self, stack_num):
        si = self.info[stack_num]

        if si.size >= si.capacity:
            self.expand(stack_num)

        # Shift all elements in stack over by one
        index = si.last_capacity_index()
        while si.is_within_capacity(index):
            self.values[index] = self.values[self.previous_index(index)]
            index = self.previous_index(index)

        # Adjust stack data.
        self.values[si.start] = None
        si.start = self.next_index(si.start)
        si.capacity -= 1

    def push(self, stack_num, value):
        if self.all_stacks_are_full():
            raise StackFullError(stack_num)

        si = self.info[stack_num]
        if si.is_full():
            self.expand(stack_num)

        si.size += 1
        self.values[si.last_element_index()] = value

    def pop(self, stack_num):
        si = self.info[stack_num]
        if si.is_empty():
            raise StackEmptyError(stack_num)

        popped = self.values[si.last_element_index()]
        self.values[si.last_element_index()] = None
        si.size -= 1
        return popped

    def peek(self, stack_num):
        si = self.info[stack_num]
        return self.values[si.last_element_index()]
