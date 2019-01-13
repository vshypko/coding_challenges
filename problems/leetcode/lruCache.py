class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashtable = {}
        self.capacity = capacity
        self.length = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashtable.keys():
            node = self.hashtable[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = DLLNode(key, value)
        if key in self.hashtable.keys():
            toRemove = self.hashtable[key]
            toRemove.prev.next = toRemove.next
            toRemove.next.prev = toRemove.prev
            self.length -= 1
        self.hashtable[key] = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        if self.length < self.capacity:
            self.length += 1
        else:
            del self.hashtable[self.tail.prev.key]
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
