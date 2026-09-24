class ListNode:
    def __init__(self,value: int):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        # self.tail = None

    def get(self, index: int) -> int:
        i = 0
        dummy = self.head
        while i <= index and dummy is not None:
            if i == index:
                return dummy.value
            dummy = dummy.next
            i += 1
        return -1 
        

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if not self.head:
            self.head = new
        else:
            dummy = self.head
            while dummy.next is not None:
                dummy = dummy.next
            dummy.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        # i = 0
        # new = ListNode(val)
        # while i <= index and not self.head:
        #     if i == index:
        if index == 0:
            dummy = ListNode(val)
            dummy.next = self.head
            self.head = dummy
        else:
            index -= 1
            i = 0
            dummy = self.head
            while i <= index and dummy is not None:
                if i == index:
                    temp_next = dummy.next
                    dummy.next = ListNode(val)
                    dummy.next.next = temp_next
                    return
                else:
                    i += 1
                    dummy = dummy.next

            
                
    def deleteAtIndex(self, index: int) -> None:
        # Edge case check
        if self.head == None: 
            return
        if index == 0:
            self.head = self.head.next
            return
        i = index - 1
        j = 0
        dummy = self.head
        while j <= i:
            if j == i:
                if dummy.next is None:
                    return
                dummy.next = dummy.next.next
                return
            else:
                dummy = dummy.next
                j += 1
        


                
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)