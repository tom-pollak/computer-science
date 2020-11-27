from linkedadt import LinkedList


class LinkedStack(LinkedList):
    def __init__(self):
        super().__init__()

    def __str__(self):
        if self._front is None:
            return 'LinkedStack([])'
        return f'LinkedStack([{str(self._front)}])'

    def push(self, value):
        super().append(value)

    def pop(self):
        if self.isempty():
            raise IndexError('Stack is empty')
        tail_node = self._tail
        self._tail = self._tail.head
        tail_node.tail = None
        return tail_node.data

    def peek(self):
        if self.isempty():
            raise IndexError('Stack is empty')
        return self._tail.data

    def append(self, *args, **kwargs):
        raise AttributeError("LinkedStack has no attribute 'append'")


class LinkedQueue(LinkedList):
    def __init__(self):
        super().__init__()

    def __str__(self):
        if self._front is None:
            return 'LinkedQueue([])'
        return f'LinkedQueue([{str(self._front)}])'

    def enqueue(self, value):
        super().append(value)

    def pop(self):
        super().pop(error='Queue is empty')

    def peek(self):
        if self.isempty():
            raise IndexError('Queue is empty')
        return self._front.data

    def append(self, *args, **kwargs):
        raise AttributeError("LinkedQueue has no attribute 'append'")


linked_stack = LinkedStack()
print(linked_stack)
linked_stack.push(1)
linked_stack.push(2)
linked_stack.push(3)
linked_stack.push(4)
print(linked_stack)
print(len(linked_stack))
print(linked_stack.pop())
print(linked_stack.pop())
print(linked_stack.pop())
print(linked_stack.pop())
print(linked_stack.pop())
