from doubly_linkedlist import Dll


class Queue:
    def __init__(self, values=None):
        self._storage = Dll(values)

    def enqueue(self, val):
        self._storage.append(val)

    def dequeue(self):
        try:
            return self._storage.pop()
        except ValueError:
            raise ValueError("The queue is empty.")

    def peek(self):
        if len(self._storage) >= 2:
            return self._storage.head.next.value
        return None

    def size(self):
        return len(self._storage)

    def __len__(self):
        return self.size()
