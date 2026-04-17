class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = None
        self.tail = None
        self.k = capacity

    def printlru(self):
        temp = self.head
        res = []
        h = self.head.key
        while temp:
            res.append(str(temp.key))
            temp = temp.next
        head = str(self.head.key) if self.head else "None"
        tail = str(self.tail.key) if self.tail else "None"
        return "LRU " + "->".join(res) + " (head:" + head + ", tail:" + tail + ")"
    
    def get(self, key: int) -> int:
        # print("get", key)
        if key in self.cache:
            node = self.cache[key]
            before = node.prev
            after = node.next
            if self.tail and self.tail.key != key: # move node to tail
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                if before:
                    before.next = after
                else:
                    self.head = after
                if after:
                    after.prev = before
            print("get", key, self.printlru())
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # update
            node = self.cache[key]
            before = node.prev
            after = node.next
            if self.tail and self.tail.key != key: # move node to tail
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                if before:
                    before.next = after
                else:
                    self.head = after
                if after:
                    after.prev = before
            node.val = value        
        else: # insert
            self.tail = ListNode(self.tail, key, value, None)
            if self.tail.prev:
                self.tail.prev.next = self.tail
            self.cache[key] = self.tail
            if len(self.cache) > self.k: # pop head
                self.cache.pop(self.head.key)
                self.head = self.head.next
                if self.head:
                    self.head.prev = None 
            if len(self.cache) == 1:
                self.head = self.tail
        print("put", key, self.printlru())

class ListNode:

    def __init__(self, prev=None, key=0, val=0, next=None):
        self.prev = prev
        self.key = key
        self.val = val
        self.next = next