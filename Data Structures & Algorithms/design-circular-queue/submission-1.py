class MyCircularQueue:

    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = None
        self.rear = None


    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity: return False

        elif self.size == 0:
            self.rear = self.Node(value)
            self.front = self.rear
            self.rear.next = self.front
        else:
            newNode = self.Node(value, self.front)
            self.rear.next = newNode
            self.rear = newNode

        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.size == 0: return False

        if self.size == 1:
            self.front = self.rear = None
        else:
            newFront = self.front.next
            self.front = None
            self.rear.next = newFront
            self.front = newFront
            

        self.size -= 1

        return True
        

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()