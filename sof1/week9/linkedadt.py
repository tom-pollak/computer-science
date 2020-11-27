class LinkedNode:
    def __init__(self, data=None, next=None, prev=None):
        self._data = data
        if next is None or isinstance(
                next, LinkedNode) and prev is None or isinstance(
                    prev, LinkedNode):
            self._next = next
            self._prev = prev
        else:
            raise TypeError('Node type object expected!')

    def __str__(self):
        """
        Note, this is a recursive method (implicit via str()). As you can see
        recursion can be used for linked list.
        """
        if self._data is None:
            return ''
        elif self._next is None:
            return str(self._data)
        else:
            return str(self._data) + ', ' + str(self._next)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def tail(self):
        return self._next

    @tail.setter
    def tail(self, node):
        if node is None or isinstance(node, LinkedNode):
            self._next = node
        else:
            raise TypeError('Node type object expected!')

    @property
    def head(self):
        return self._prev

    @head.setter
    def head(self, node):
        if node is None or isinstance(node, LinkedNode):
            self._prev = node
        else:
            raise TypeError('Node type object expected!')


class LinkedList:
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def __str__(self):
        if self._front is None:
            return 'LinkedList([])'
        else:
            return 'LinkedList([' + str(self._front) + '])'

    def __len__(self):
        """
        Rather than traversing the list from front to end, it is better to have an attribute _size
        that is updated every time we add or remove an element.
        The code below shows you how to traverse a linked list, from start to end.
        To traverse the list, we need to use a local variable <currentnode> to move along the list,
        we must not change/move the pointer _front.
            count = 0
            currentnode = self._front
            while currentnode is not None:
                count += 1
                currentnode = currentnode._next

        """
        return self._size

    def __getitem__(self, index):
        if index >= self._size:
            return IndexError('Index out of range')
        node = self._front
        for i in range(index + 1):
            node = node.tail
        return node.data

    def __setitem__(self, index, value):
        node = self.__getitem__(index)
        node.data = value

    def __contains__(self, key):
        node = self._front
        for i in range(self._size):
            if node.data == key:
                return True
            node = node.tail
        return False

    def isempty(self):
        return self._size == 0

    def append(self, value):
        new_node = LinkedNode(value)
        if self._front is None:
            self._front = new_node
            self._tail = new_node
        else:
            self._tail.tail = new_node
            self._tail = new_node

        self._size += 1

    def pop(self, error='List is empty'):
        if self.isempty():
            raise IndexError(error)

        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -= 1
        return front_node.data

    def clear(self):
        self._front = None
        self._tail = None
        self._size = 0

    def index(self, value, start=0, stop=2147483647):
        node = self._front
        for i in range(start, stop):
            if node.data == value:
                return i
            node = node.tail
        raise ValueError('Value not found')

    def insert(self, index, object):
        node = self._front
        if not isinstance(object, LinkedNode):
            raise TypeError('LinkedNode object expected!')
        for i in range(index + 1):
            node = node.tail
            print(node)
        object.tail, node.head = node.head, object
        object.head, object.tail.head = object.tail.head, object

    def remove(self, value):
        node = self.index(value=value)
        node.head.tail, node.tail.head = node.tail.head, node.head.tail


linkedlist = LinkedList()
print(linkedlist)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
print(linkedlist)
print(len(linkedlist))
print(linkedlist.pop())
print(linkedlist.pop())
print(linkedlist.pop())
print(linkedlist.pop())
print(linkedlist.pop())
