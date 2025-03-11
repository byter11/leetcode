class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [0] * k
        self.front = self.rear = -1
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.front = self.rear = self.nextFront()
        else: 
            self.front = self.nextFront()
        self.dq[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.front = self.rear = self.nextRear()
        else:
            self.rear = self.nextRear()
        self.dq[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.dq[self.front] = 0

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = self.prevFront()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.dq[self.rear] = 0

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = self.prevRear()
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.dq[self.front]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.dq[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1 and self.rear == -1

    def isFull(self) -> bool:
        return self.nextRear() == self.front
    
    def nextRear(self) -> int:
        return 0 if self.rear == -1 else (self.rear + 1) % self.k

    def nextFront(self) -> int:
        return 0 if self.front == -1 else self.k - 1 if self.front == 0 else self.front - 1

    def prevRear(self) -> int:
        return 0 if self.rear == -1 else self.k - 1 if self.rear == 0 else self.rear - 1

    def prevFront(self) -> int:
        return 0 if self.front == -1 else (self.front + 1) % self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()