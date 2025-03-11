class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class MyCalendar:
    def __init__(self):
        self.books = None

    def book(self, start: int, end: int) -> bool:
        if not self.books:
            self.books = Node([start, end])
            return True
        
        # print('inserting: ', [start, end])
        p = self.books
        last = p
        while p:
            last = p
            # print(last.val)
            if ((start >= last.val[0] and start < last.val[1]) or (end > last.val[0] and end <= last.val[1]) 
            or (last.val[0] >= start and last.val[0] < end) or (last.val[1] > start and last.val[1] <= end)):
                # print("noo")
                return False
            if p.val[0] > start:
                p = p.left
            else:
                p = p.right
        
        # print("")
        if last.val[0] > start: 
            last.left = Node([start, end])
        else:
            last.right = Node([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# [97, 100] [33,51] [75,92] [19,30][53,63], 

# [97,100],[33,51],[75,92],[19,30],[53,63],[13,32]]
# [true,true,true,true,true,true]